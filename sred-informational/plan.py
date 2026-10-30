#!/usr/bin/env python3
"""Turn one page's audit rows into minimal, verified edit operations.

Usage: plan.py <id> <fetch_result_file> [--max 480]

<fetch_result_file> is the saved output of wp_get_post_full (context edit, include meta,
meta_keys _elementor_edit_mode,_elementor_data). Writes apply/ops/<id>.json:
  {"id", "editor", "ops": [{"row", "search", "replace", "regex"}], "skipped": [...]}
Each op is checked in order against the current string: a literal search occurs exactly once,
a regex search matches exactly once and covers the same span. Replaying the ops gives the same
result as applying the audit rows in full. Rows flagged needs_sharad, manual and rank_math are skipped.
With --sharad, approved needs_sharad rows are included too and ops go to apply/ops-sharad/<id>.json.
"""
import hashlib, json, re, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_source(path):
    d = json.load(open(path))
    post = d.get("post", d)
    meta = d.get("meta") or {}
    if meta.get("_elementor_edit_mode") == "builder":
        return "elementor", meta["_elementor_data"]
    c = post["content"]
    return "post_content", c["raw"] if isinstance(c, dict) else c


def shrink(s, before, after, limit, minlen=3):
    """Smallest unique (search, replace) inside `before` that turns s into the same result."""
    i = s.index(before)
    p = 0
    while p < min(len(before), len(after)) and before[p] == after[p]:
        p += 1
    q = 0
    while q < min(len(before), len(after)) - p and before[-1 - q] == after[-1 - q]:
        q += 1
    lo, hi = i + p, i + len(before) - q          # changed span in s
    rep = after[p:len(after) - q]
    pad = 0
    while True:
        a, b = max(i, lo - pad), min(i + len(before), hi + pad)
        cand = s[a:b]
        if (len(cand) >= minlen or (a == i and b == i + len(before))) and s.count(cand) == 1:
            return cand, s[a:lo] + rep + s[hi:b], a, b
        if a == i and b == i + len(before):
            raise ValueError("before is not unique")
        pad += 8


def regex_op(s, a, b, replace):
    """Regex covering exactly s[a:b] with literal head/tail, for spans over the limit."""
    for n in (60, 100, 150, 200, 230):
        head, tail = s[a:a + n], s[b - n:b]
        pat = re.escape(head) + r"[\s\S]*?" + re.escape(tail)
        if len(pat) > 500:
            break
        ms = list(re.finditer(pat, s))
        if len(ms) == 1 and ms[0].span() == (a, b):
            return pat, replace.replace("\\", "\\\\").replace("$", "\\$")
    raise ValueError("no unique regex within 500 chars")


def main():
    pid, src = sys.argv[1], sys.argv[2]
    limit = int(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 480
    audit = json.load(open(os.path.join(HERE, "audit", f"{pid}.json")))
    editor, s = load_source(src)
    sharad = "--sharad" in sys.argv
    outdir = os.path.join(HERE, "apply", "ops-sharad" if sharad else "ops")
    full = s
    ops, skipped = [], []
    for n, r in enumerate(audit["rows"]):
        if (r.get("needs_sharad") and not sharad) or r["editor"] not in ("elementor", "post_content"):
            skipped.append({"row": n, "why": "needs_sharad" if r.get("needs_sharad") else r["editor"]})
            continue
        if r["editor"] != editor:
            skipped.append({"row": n, "why": f"row is {r['editor']}, page renders from {editor}"})
            continue
        if r["before"] in r["after"] and r["after"] in full:
            skipped.append({"row": n, "why": "already live (after text present)"})
            continue
        if full.count(r["before"]) != 1:
            skipped.append({"row": n, "why": f"before found {full.count(r['before'])} times now"})
            continue
        full = full.replace(r["before"], r["after"], 1)
        search, replace, a, b = shrink(s, r["before"], r["after"], limit, 80 if editor == "elementor" else 3)
        op = {"row": n, "search": search, "replace": replace, "regex": False}
        if editor == "post_content" and len(search) > limit:
            op["search"], op["replace"] = regex_op(s, a, b, replace)
            op["regex"] = True
        s = s[:a] + replace + s[b:]
        ops.append(op)
    assert s == full, "replayed ops differ from the audit result"
    if editor == "elementor":
        json.loads(s)  # the edited Elementor data must still parse
    os.makedirs(outdir, exist_ok=True)
    out = {"id": int(pid), "editor": editor, "sha256_after": hashlib.sha256(s.encode()).hexdigest(),
           "ops": ops, "skipped": skipped}
    json.dump(out, open(os.path.join(outdir, f"{pid}.json"), "w"), indent=1, ensure_ascii=False)
    print(f"{pid} {editor} ops={len(ops)} skipped={len(skipped)} regex={sum(o['regex'] for o in ops)}")


if __name__ == "__main__":
    main()
