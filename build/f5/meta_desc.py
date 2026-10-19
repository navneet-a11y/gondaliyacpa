"""SEO meta descriptions for the 16 items published 2026-10-19.

Delivery route. Rank Math's own `rank_math_description` is not registered with
show_in_rest, so the connector cannot write it (confirmed: the key came back in
`ignored_keys`). The writable lever is the WordPress excerpt, which is what Rank
Math's description template falls back to by default and what page 904 already
uses. Navneet confirms in Rank Math > Titles & Meta that the description
template for these post types is %excerpt%.

Length. Capped at 155 characters, because that is roughly where Google truncates.
This deviates from plan line 1166 ("the answer-first paragraph IS the meta
description"), whose 40-to-60-word paragraphs run 250 to 300 characters and would
be cut mid-sentence. The plan's intent, the answer visible in the snippet, is
better served by a shorter line that shows in full. Logged in decisions.md.

Compliance. Same hard rules as the pages. Note entry 18: a meta description
cannot carry the 7.4 qualification block, so its description states what applies
rather than making the bare claim hard rule 3 forbids.
"""
import re, sys

PRICE = '$300.00 plus HST per tax year'

DESC = {
 # Family 5, items 925 to 934
 925: ('do-i-need-to-file-a-t2-for-the-year-my-corporation-was-dissolved',
   'Yes. A final T2 covers the fiscal year up to the dissolution date and is '
   'due within six months of dissolution. Filed at $300.00 plus HST per tax year.'),
 926: ('do-i-need-a-business-number-to-file-a-nil-t2',
   "Yes. The return is filed against the corporation's nine-digit business "
   'number and its RC corporation income tax account. $300.00 plus HST per tax year.'),
 927: ('do-i-need-to-file-a-nil-t2-if-i-never-started-operating',
   'Yes. The first tax year begins on the incorporation date, not the day '
   'trading starts, so a nil return is due. $300.00 plus HST per tax year.'),
 928: ('do-i-need-to-file-a-t2-every-year-if-my-corporation-is-inactive',
   'Yes, every year. Inactive is a description, not a filing status, so the T2 '
   'is due until dissolution. $300.00 plus HST per tax year.'),
 929: ('can-i-file-five-years-of-nil-t2-returns-at-once',
   'Yes. Five missed year-ends mean five separate returns, transmitted in one '
   'pass, oldest first. $300.00 plus HST per tax year, so $1,500.00 for five.'),
 930: ('can-i-file-a-nil-t2-myself-without-an-accountant',
   'Yes. Nothing requires a corporation to use an accountant. What a self-filed '
   'T2 still needs, and what CPA review at $300.00 plus HST adds.'),
 931: ('can-i-dissolve-my-corporation-with-unfiled-t2-returns',
   'Not cleanly. A clearance certificate cannot be issued until every return is '
   'filed, and the unfiled years stay due after dissolution.'),
 932: ('can-i-file-a-nil-t2-late-without-a-penalty',
   'What actually applies when a nil T2 is filed late: the open year, the demand '
   'to file, the blocked clearance certificate and the non-resident daily amount.'),
 933: ('can-i-file-nil-t2-returns-for-a-corporation-i-forgot-about',
   'Yes. Every year since incorporation can still be filed. Confirm the registry '
   'status and the fiscal year-end first. $300.00 plus HST per tax year.'),
 934: ('can-i-still-file-a-t2-after-my-corporation-was-dissolved',
   'Yes. The final return is due within six months of the dissolution date, and '
   'earlier unfiled years can still be filed. $300.00 plus HST per tax year.'),
 # Family 9, items 945 to 955
 945: ('dormant-and-inactive-corporations',
   'What dormant means to the CRA, which returns a dormant corporation still '
   'files, what keeps it compliant, and when to wind it up. CPA reviewed.'),
 947: ('catch-up-unfiled-corporate-tax-returns',
   'How many years can still be filed, the order to file them in, what a demand '
   'to file means, and what the catch-up costs at $300.00 plus HST per year.'),
 949: ('final-t2-and-dissolution',
   'When the final T2 is due, what period it covers, why a clearance certificate '
   'matters, and what must be filed before a corporation can close.'),
 951: ('t2-short-eligibility',
   'The eight conditions for the two-page T2 Short, what disqualifies a '
   'corporation, and which schedules are still required either way.'),
 953: ('provincial-and-federal-annual-returns',
   'The Ontario annual return, the $12.00 Corporations Canada annual return, '
   'Alberta AT1 and Quebec CO-17, and why the T2 covers none of them.'),
 955: ('t183corp-signing-and-transmission',
   'What Form T183CORP authorises, who may sign it, when and how it is signed, '
   'how long it is kept, and what EFILE transmission involves.'),
}

BANNED = ['cheapest', 'lowest price', 'best price', 'unbeatable', 'guarantee',
          'risk-free', 'risk free', 'fastest', 'instant filing', 'no obligation',
          'penalty free', 'penalty-free', 'zero penalty', 'no penalty',
          'authorized', 'authorised', 'cra agent', 'cra approved', 'cra partner',
          'cra endorsed', 'book a call', 'calendly', 'starting from', 'simply',
          'easily', 'such as', ' just ']

fail = []
for pid, (slug, d) in sorted(DESC.items()):
    n = len(d)
    if n > 155:
        fail.append('%d: %d chars, cap is 155' % (pid, n))
    if n < 110:
        fail.append('%d: %d chars, too short to be useful' % (pid, n))
    low = d.lower()
    for b in BANNED:
        if b in low:
            fail.append('%d: banned phrase "%s"' % (pid, b.strip()))
    if re.search(r'T183(?!CORP)', d):
        fail.append('%d: bare T183' % pid)
    if 'including HST' in d:
        fail.append('%d: "including HST" contradicts the standing correction' % pid)
    if any(ord(c) > 0x2100 for c in d):
        fail.append('%d: non-ASCII symbol that may be an emoji' % pid)
    if any(ord(c) > 127 for c in d):
        fail.append('%d: non-ASCII character' % pid)
    # hard rule 3: no bare penalty claim without the block, which cannot fit here
    if 'penalt' in low and 'no percentage' not in low:
        if re.search(r'(no|without|free of|zero)\s+\w*\s*penalt', low):
            fail.append('%d: bare penalty claim in a meta description' % pid)

if len({d for _s, d in DESC.values()}) != len(DESC):
    fail.append('duplicate descriptions')

if fail:
    print('DESC GATE FAILED')
    for f in fail:
        print(' -', f)
    sys.exit(1)

print('all %d descriptions clear' % len(DESC))
for pid, (slug, d) in sorted(DESC.items()):
    print('%4d  %3d  %-62s' % (pid, len(d), slug[:62]))
