"""Rank Math meta for guides 28 to 30, validated before it is applied.

Same convention as batch 5: the word "penalty" is avoided in every
description. Hard rule 3 requires a penalty claim to carry the full
qualification block, and a 160-character description cannot hold it, so the
meta stays off the subject and the page body carries the qualified statement.
"""
SEO = {
 'cra-accounts-on-a-dormant-corporation': (
  'CRA Accounts on a Dormant Corporation | Guide',
  'A business number carries separate accounts, and each keeps its own '
  'obligations until it is closed. What is still owed, and how to end it.',
  'cra accounts dormant corporation'),
 'choosing-and-changing-a-fiscal-year-end': (
  'Choosing and Changing a Fiscal Year-End | Guide',
  'A corporation picks its own year-end and the first return fixes it. How to '
  'choose it, the 53-week limit, and what a change costs.',
  'changing a fiscal year end'),
 'quebec-co17-and-alberta-at1': (
  'Quebec CO-17 and Alberta AT1 | Complete Guide',
  'Quebec and Alberta each collect their own corporate tax, so each has a '
  'separate return. CO-17 and AT1 are not part of the federal T2.',
  'quebec co-17 and alberta at1'),
}

for _s, (_t, _d, _k) in SEO.items():
    assert len(_t) <= 60, '%s: title is %d characters' % (_s, len(_t))
    assert 70 <= len(_d) <= 160, '%s: description is %d characters' % (_s, len(_d))
    assert 'penalty' not in _d.lower(), '%s: description mentions a penalty' % _s
    assert _k == _k.lower(), '%s: keyword is not lower case' % _s

if __name__ == '__main__':
    for _s, (_t, _d, _k) in SEO.items():
        print('%-42s t%-3d d%-4d %s' % (_s, len(_t), len(_d), _k))
