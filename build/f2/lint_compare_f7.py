# -*- coding: utf-8 -*-
"""Refuse a duplicate key in any COMPARE_F7 map.

Python dict literals let the LAST duplicate key win, silently, so a second
entry for a slug drops the first one's comparison links without any error. It
happened on 2026-11-05: build_f2c.py gained a second
'dissolution-readiness-checker' key and the new link would have vanished. No
runtime assert can catch it, because the duplicate is gone before the dict
exists. So this reads the source.
"""
import glob, io, re, sys

bad = 0
for f in sorted(glob.glob('build_f2*.py')):
    src = io.open(f, encoding='utf-8').read()
    m = re.search(r'^COMPARE_F7 = \{.*?^\}', src, re.S | re.M)
    if not m:
        continue
    keys = re.findall(r"^ '([a-z0-9-]+)':", m.group(0), re.M)
    dups = sorted({k for k in keys if keys.count(k) > 1})
    print('%-16s %2d keys%s' % (f, len(keys),
                                '  DUPLICATE: ' + ', '.join(dups) if dups else ''))
    if dups:
        bad += 1
if bad:
    print('\n%d builder(s) with a duplicate COMPARE_F7 key' % bad)
    sys.exit(1)
print('\nno duplicate COMPARE_F7 keys')
