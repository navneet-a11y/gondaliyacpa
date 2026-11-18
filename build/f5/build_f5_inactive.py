#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Family 5: /answers/does-an-inactive-corporation-have-to-file-a-t2/

Navneet, 2026-11-18: "now create answer page detailed same way does an
inactive corporation have to file a t2 beat top ranking", with the canada.ca
T2 guide, the H&R Block post and the live AI Overview supplied as the targets.

THIS REVERSES A RECORDED DECISION
---------------------------------
build_f5_esign.py says of this exact slug: "Covered. ID 928 ... is the same
question, and ID 858 ... overlaps it. Building it would cannibalise 928, which
6(k)'s internal rule forbids. NOT BUILT." That judgement is reversed here on
Navneet's instruction, and the reasons it is defensible are recorded rather
than assumed:

  - 6(d) line 1270 names this URL as the Family 5 head term, 480 monthly
    searches, and calls it the "top AI Overviews candidate". 6(d) line 1166
    fixes its title, H1 and answer paragraph. Appendix A names the slug.
  - 928 and 858 have drawn ZERO impressions in the October 1 to November 17
    window, so nothing that works is being displaced.
  - The cannibalisation is handled rather than ignored: 928, 858 and
    /answers/how-do-i-know-if-my-corporation-counts-as-dormant/ now link up to
    this page as the full answer, and 6(k) is measured below rather than
    assumed.

If 6(k) had come out above 0.60 the right answer would have been to
canonicalise 858 and 928 onto this page instead. The measured figure is in
docs/decisions.md.

THE ANSWER PARAGRAPH IS THE PLAN'S
----------------------------------
Line 1584 gives the copy-paste answer block filled for this very URL, and line
1166 says the answer-first paragraph is the meta description. Both are used
verbatim. It is 51 words, inside the 40 to 60 that line 1213 fixes.

BEATING THE SUPPLIED SOURCES
----------------------------
The AI Overview answers five things: that it applies every year, the narrow
exceptions, that the T2 Short may be used, the six-month deadline, and what
happens if you do not file. The table carries all five as extractable rows and
the extra sections cover each in prose, which is what the answer-first template
alone could not do. The 'extra' key was added to build_f5.build() for this, and
the other forty-five pages render byte-identical without it.

TWO FACTS THIS PAGE PUBLISHES FIRST, AND ONE IT DOES NOT
--------------------------------------------------------
The exceptions - a tax-exempt Crown corporation, a Hutterite colony and a
registered charity - appear nowhere else on this site. They are the Canada
Revenue Agency's own list from the T2 guide Navneet supplied, and a page whose
whole job is "does this apply to me" cannot answer honestly without them.
**They are flagged for Sharad Gondaliya's sign-off in docs/decisions.md**,
because the house rule is that a page should not be the first place a fact
appears on this site.

What this page does NOT copy is the AI Overview's penalty sentence. It states
$25 per day to $2,500 under subsection 162(7) as applying generally. Section
7.4's qualification block, mandatory wherever a penalty is mentioned, scopes
that figure to a non-resident-owned corporation. The block is used unchanged
and the broader claim is not made.
"""
import io, json, os

import build_f5 as b
from build_f5 import build, a, SITE, PRICE

HERE = os.path.dirname(os.path.abspath(__file__))
SLUG = 'does-an-inactive-corporation-have-to-file-a-t2'
DATE, ISO = 'November 18, 2026', '2026-11-18'

# National page: Navneet's 2026-11-12 ruling. The other forty-five keep the
# HST wording until the sweep in docs/decisions.md.
FEE = '$300.00 plus applicable sales tax per tax year'
FEE_TITLE = '$300.00 Plus Applicable Sales Tax Per Tax Year'

CMP = SITE + '/compare/nil-t2-filing-vs-t2-short-filing/'
ELIG = SITE + '/tools/t2-short-eligibility-checker/'

REC = dict(
 slug=SLUG,
 h1='Does an Inactive Corporation Have to File a T2?',
 anchor='Does an inactive corporation have to file',
 keyword='does an inactive corporation have to file a t2',
 price=FEE, price_title=FEE_TITLE,
 date=DATE, iso=ISO, wrap=True,
 # Line 1584, verbatim. Line 1166 makes it the meta description too.
 answer=('Yes. Every resident corporation, including an inactive one, must '
         'file a T2 return within six months of its fiscal year-end, every '
         'year, until it is formally dissolved. A final T2 is due within six '
         'months of dissolution. Having no revenue, no bank activity and no '
         'employees does not remove the obligation.'),
 head=('What applies', 'Position'),
 rows=[('Corporations that must file',
        'Every resident corporation, whether or not it did anything'),
       ('How often', 'Every tax year the corporation exists'),
       ('Months after the fiscal year-end to file', '6'),
       ('Narrow exceptions',
        'A tax-exempt Crown corporation, a Hutterite colony, a registered '
        'charity'),
       ('Tax owing on a true nil return', '$0.00'),
       ('Form where all eight short-return conditions are met', 'T2 Short'),
       ('When the obligation ends',
        'On formal dissolution, after a final T2'),
       ('Fee to file', FEE)],
 qual=True,
 body=('Inactive is a description of what the corporation did, not a status '
       'the Canada Revenue Agency recognises. There is no form that pauses '
       'the T2 while a corporation sits idle, and no income level below which '
       'the year can be skipped. The duty comes from being an incorporated '
       'resident corporation, and it runs for every year the corporation is '
       'on the register.'),
 extra=[
  ('The Exceptions Are Narrow',
   ['Three kinds of corporation are outside the rule: a tax-exempt Crown '
    'corporation, a Hutterite colony, and a registered charity. Everything '
    'else files, including a non-profit organisation and a corporation that '
    'has never traded.',
    'An ordinary numbered company that stopped trading is not in any of those '
    'three categories, so it keeps filing. So does a shelf corporation that '
    'has never opened a bank account, and a holding corporation whose only '
    'asset is a single share it has held for years.']),
  ('Inactive, Dormant and Nil Are Not the Same Word',
   ['Inactive and dormant describe the corporation. Nil describes one tax '
    'year of it, and it is decided year by year: a corporation can be nil for '
    'three years, earn something in the fourth, and be nil again in the '
    'fifth.',
    'The distinction matters because a year that looks quiet is not always '
    'nil. Investment income, rental income, and a dividend paid or received '
    'each break it, even where nothing else moved and the bank statement is '
    'empty.']),
  ('Which Form the Return Goes On',
   ['A corporation that meets all eight of the Canada Revenue Agency&rsquo;s '
    'conditions for the short return may file the two-page T2 Short '
    'instead of the full T2. Most quiet years meet them, but the test is '
    'run against each year on its own.',
    'That is a separate question from whether the year is nil at all, which '
    'is set out in ' + a(CMP, 'nil T2 filing vs T2 Short filing')
    + '. The ' + a(ELIG, 'T2 Short eligibility checker')
    + ' runs all eight conditions in one screen.']),
  ('How the Obligation Ends',
   ['Only formal dissolution stops it. Letting a corporation lapse, closing '
    'its bank account or simply not filing does none of that: the corporation '
    'stays on the register and each year it does not file stays open.',
    'Dissolution needs the earlier years filed first, because an unfiled year '
    'blocks the clearance certificate, and the clearance certificate is what '
    'confirms nothing is owed before the corporation closes. The last tax '
    'year ends on the dissolution date and its final T2 is due six months '
    'after it.']),
 ],
)

SIBLINGS = [
 ('do-i-need-to-file-a-t2-every-year-if-my-corporation-is-inactive',
  'Do I need to file every year'),
 ('do-i-need-to-file-a-t2-if-my-corporation-had-no-activity',
  'Do I need to file with no activity'),
 ('how-do-i-know-if-my-corporation-counts-as-dormant',
  'How do I know if it counts as dormant'),
 ('what-happens-if-i-dont-file-a-nil-t2',
  'What happens if I do not file'),
]


if __name__ == '__main__':
    # build_f5 rebuilds its forty-five on import. Prove the two new keys change
    # nothing for a record that passes neither.
    import subprocess
    _dirty = subprocess.run(['git', 'status', '--porcelain', '--',
                             'build/f5/'], cwd=os.path.join(HERE, '..', '..'),
                            capture_output=True, text=True).stdout
    _unexpected = [l for l in _dirty.splitlines()
                   if not any(k in l for k in
                              ('build_f5.py', 'gate.py', 'f5-manifest.json',
                               'build_f5_inactive.py', SLUG,
                               'do-i-need-to-file-a-t2-every-year',
                               'do-i-need-to-file-a-t2-if-my-corporation',
                               'how-do-i-know-if-my-corporation'))]
    assert not _unexpected, (
        'the extra/price keys changed a page that passes neither:\n'
        + '\n'.join(_unexpected))

    sibs = [dict(slug=s, anchor=an) for s, an in SIBLINGS]
    html, url = build(REC, sibs)
    assert 'plus HST' not in html, 'a national page may not name HST'
    assert REC['answer'] in html
    assert 40 <= len(REC['answer'].split()) <= 60, len(REC['answer'].split())

    io.open(os.path.join(HERE, SLUG + '.html'), 'w',
            encoding='utf-8').write(html)

    mf = os.path.join(HERE, 'f5-manifest.json')
    recs = json.load(io.open(mf, encoding='utf-8'))
    recs = [r for r in recs if r['slug'] != SLUG]
    recs.append(dict(slug=SLUG, title=REC['h1'], meta_description=REC['answer'],
                     url=url, content=html, answer=REC['answer'],
                     keyword=REC['keyword'], anchor=REC['anchor'],
                     terms={'cnf_family': ['f5']},
                     meta={'cnf_question_text': REC['h1'],
                           'cnf_short_answer': REC['answer'],
                           'cnf_primary_keyword': REC['keyword'],
                           'cnf_last_verified_et': ISO}))
    json.dump(recs, io.open(mf, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print('%s\n  %d bytes, answer %d words, %d records in the manifest'
          % (SLUG, len(html.encode()), len(REC['answer'].split()), len(recs)))
