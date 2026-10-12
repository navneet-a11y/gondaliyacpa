#!/usr/bin/env python3
"""Verify the keyword bank in an industry brief.

Usage: python3 scripts/verify_keyword_bank.py <brief.md> [...]

Reads lines of the form

    **C1 · Primary + CPA (10)** — keyword one, keyword two, ...

and checks each cluster's keyword count against the locked bank shape, that the
bank totals 148 keywords, and that no keyword is repeated.  Commas inside
numbers ($1,250,000) are protected so such a keyword is not split in two.
"""
import re
import sys

EXPECTED = {
    "C1": 10, "C2": 8, "C3": 12, "C4": 10, "C5": 20, "C6": 8,
    "C7": 8, "C8": 20, "C9": 15, "C10": 17, "C11": 20,
}
TOTAL = sum(EXPECTED.values())  # 148

CLUSTER_RE = re.compile(r"\*\*(C\d+)[^(]*\((\d+)\)\*\*\s*—\s*(.+)")
NUM_COMMA_RE = re.compile(r"(?<=\d),(?=\d)")
SENTINEL = "\x00"


def split_keywords(blob):
    """Split a cluster's keyword list on commas, keeping $1,250,000 in one piece."""
    protected = NUM_COMMA_RE.sub(SENTINEL, blob)
    out = []
    for chunk in protected.split(","):
        kw = chunk.replace(SENTINEL, ",").strip()
        if kw:
            out.append(kw)
    return out


def parse(path):
    clusters = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            m = CLUSTER_RE.search(line)
            if m:
                cid, declared, blob = m.group(1), int(m.group(2)), m.group(3)
                clusters.append((cid, declared, split_keywords(blob)))
    return clusters


def verify(path):
    clusters = parse(path)
    print(path)
    if not clusters:
        print("   no keyword clusters found")
        print("   TOTAL: 0  FAIL")
        print("   duplicates: none")
        return False

    total = 0
    mismatches = 0
    seen = {}
    for cid, declared, keywords in clusters:
        n = len(keywords)
        total += n
        want = EXPECTED.get(cid)
        problems = []
        if want is None:
            problems.append("unexpected cluster")
        elif n != want:
            problems.append("expected %d" % want)
        if declared != n:
            problems.append("header says %d" % declared)
        if problems:
            mismatches += 1
            print("   %-6s%2d  MISMATCH (%s)" % (cid, n, "; ".join(problems)))
        else:
            print("   %-6s%2d  ok" % (cid, n))
        for kw in keywords:
            seen[kw.lower()] = seen.get(kw.lower(), 0) + 1

    missing = [c for c in EXPECTED if c not in {c for c, _, _ in clusters}]
    for cid in sorted(missing, key=lambda c: int(c[1:])):
        mismatches += 1
        print("   %-6s%2d  MISMATCH (cluster absent, expected %d)" % (cid, 0, EXPECTED[cid]))

    ok = total == TOTAL and mismatches == 0
    print("   TOTAL: %d  %s" % (total, "PASS" if ok else "FAIL"))

    dupes = sorted(k for k, c in seen.items() if c > 1)
    if dupes:
        print("   duplicates: %s" % ", ".join(dupes))
        ok = False
    else:
        print("   duplicates: none")
    return ok


def main(argv):
    if len(argv) < 2:
        sys.exit("usage: verify_keyword_bank.py <brief.md> [...]")
    ok = True
    for path in argv[1:]:
        ok = verify(path) and ok
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
