#!/usr/bin/env python3
"""check.py <id> <fetch_result_file>: after applying, confirm the live string equals the planned result."""
import hashlib, json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from plan import load_source
pid, src = sys.argv[1], sys.argv[2]
plan = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "apply", "ops-sharad" if "--sharad" in sys.argv else "ops", f"{pid}.json")))
editor, s = load_source(src)
if editor == "elementor":
    json.loads(s)
ok = hashlib.sha256(s.encode()).hexdigest() == plan["sha256_after"]
print(pid, "MATCH" if ok else "DIFFERS")
