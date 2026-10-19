"""Paste-ready Rank Math fields for every page published in this session,
plus tightened descriptions for the ten answer pages whose line 1166
descriptions run 250 to 300 characters and truncate in search results.

Lengths: title target <= 60 characters, description target <= 155.
Where the question itself exceeds 60, a tightened alternative is offered and
the exact-match question is kept as the H1 on the page either way.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = 'https://corpnilfilingfor300.ca'

# slug -> (seo_title, tightened_title_or_None, description, focus_keyword)
ROWS = []

def add(url, title, short, desc, kw):
    ROWS.append((url, title, short, desc, kw))

# ---- Family 9 guides -------------------------------------------------------
add('/guides/nil-t2-return-complete-guide/',
    'Nil T2 Return | Complete Guide for Canadian Corporations', None,
    'Who must file, what a nil return is, which schedules are required, how '
    'T183CORP is signed, and what happens to unfiled years.',
    'nil t2 return')
add('/guides/dormant-and-inactive-corporations/',
    'Dormant Corporations | Complete Filing Guide for Canada', None,
    'What dormant means to the CRA, which returns a dormant corporation still '
    'files, what keeps it compliant, and when to wind it up. CPA reviewed.',
    'dormant corporation')
add('/guides/catch-up-unfiled-corporate-tax-returns/',
    'Unfiled Corporate Tax Returns | Catch-Up Guide for Canada', None,
    'How many years can still be filed, the order to file them in, what a demand '
    'to file means, and what the catch-up costs at $300.00 plus HST per year.',
    'unfiled corporate tax returns')
add('/guides/final-t2-and-dissolution/',
    'Final T2 and Dissolution | Guide for Canadian Corporations',
    'Final T2 and Dissolution | Complete Canadian Guide',
    'When the final T2 is due, what period it covers, why a clearance certificate '
    'matters, and what must be filed before a corporation can close.',
    'final t2 before dissolution')
add('/guides/t2-short-eligibility/',
    'T2 Short | Eligibility Guide for Canadian Corporations', None,
    'The eight conditions for the two-page T2 Short, what disqualifies a '
    'corporation, and which schedules are still required either way.',
    't2 short')
add('/guides/provincial-and-federal-annual-returns/',
    'Provincial and Federal Annual Returns | Canadian Guide',
    'Annual Returns | Ontario, Federal, AT1 and CO-17',
    'The Ontario annual return, the $12.00 Corporations Canada annual return, '
    'Alberta AT1 and Quebec CO-17, and why the T2 covers none of them.',
    'ontario annual return')
add('/guides/t183corp-signing-and-transmission/',
    'Form T183CORP | Signing and Transmission Guide', None,
    'What Form T183CORP authorises, who may sign it, when and how it is signed, '
    'how long it is kept, and what EFILE transmission involves.',
    't183corp')

# ---- Family 16 hub ---------------------------------------------------------
add('/guides/',
    'Nil T2 Filing Guides for Canadian Corporations', None,
    'In-depth guides to filing a nil T2 corporate return in Canada, written and '
    'reviewed by a CPA Ontario member. $300.00 plus HST per tax year.',
    'nil t2 filing guide')

# ---- Family 5, items 925 to 934 (set this session) -------------------------
add('/answers/do-i-need-to-file-a-t2-for-the-year-my-corporation-was-dissolved/',
    'Do I Need to File a T2 for the Year My Corporation Was Dissolved?',
    'Do I File a T2 for the Year My Corporation Dissolved?',
    'Yes. A final T2 covers the fiscal year up to the dissolution date and is due '
    'within six months of dissolution. Filed at $300.00 plus HST per tax year.',
    't2 for the year my corporation was dissolved')
add('/answers/do-i-need-a-business-number-to-file-a-nil-t2/',
    'Do I Need a Business Number to File a Nil T2?', None,
    "Yes. The return is filed against the corporation's nine-digit business number "
    'and its RC corporation income tax account. $300.00 plus HST per tax year.',
    'business number to file a nil t2')
add('/answers/do-i-need-to-file-a-nil-t2-if-i-never-started-operating/',
    'Do I Need to File a Nil T2 if I Never Started Operating?', None,
    'Yes. The first tax year begins on the incorporation date, not the day trading '
    'starts, so a nil return is due. $300.00 plus HST per tax year.',
    'nil t2 never started operating')
add('/answers/do-i-need-to-file-a-t2-every-year-if-my-corporation-is-inactive/',
    'Do I Need to File a T2 Every Year if My Corporation Is Inactive?',
    'Do I File a T2 Every Year if My Corporation Is Inactive?',
    'Yes, every year. Inactive is a description, not a filing status, so the T2 is '
    'due until dissolution. $300.00 plus HST per tax year.',
    't2 every year corporation inactive')
add('/answers/can-i-file-five-years-of-nil-t2-returns-at-once/',
    'Can I File Five Years of Nil T2 Returns at Once?', None,
    'Yes. Five missed year-ends mean five separate returns, transmitted in one '
    'pass, oldest first. $300.00 plus HST per tax year, so $1,500.00 for five.',
    'file five years of nil t2 returns')
add('/answers/can-i-file-a-nil-t2-myself-without-an-accountant/',
    'Can I File a Nil T2 Myself Without an Accountant?', None,
    'Yes. Nothing requires a corporation to use an accountant. What a self-filed '
    'T2 still needs, and what CPA review at $300.00 plus HST adds.',
    'file a nil t2 without an accountant')
add('/answers/can-i-dissolve-my-corporation-with-unfiled-t2-returns/',
    'Can I Dissolve My Corporation With Unfiled T2 Returns?', None,
    'Not cleanly. A clearance certificate cannot be issued until every return is '
    'filed, and the unfiled years stay due after dissolution.',
    'dissolve corporation with unfiled t2 returns')
add('/answers/can-i-file-a-nil-t2-late-without-a-penalty/',
    'Can I File a Nil T2 Late Without a Penalty? What Applies',
    None,
    'What actually applies when a nil T2 is filed late: the open year, the demand '
    'to file, the blocked clearance certificate and the non-resident daily amount.',
    'file a nil t2 late')
add('/answers/can-i-file-nil-t2-returns-for-a-corporation-i-forgot-about/',
    'Can I File Nil T2 Returns for a Corporation I Forgot About?',
    'Can I File Nil T2 Returns for a Forgotten Corporation?',
    'Yes. Every year since incorporation can still be filed. Confirm the registry '
    'status and the fiscal year-end first. $300.00 plus HST per tax year.',
    'nil t2 for a forgotten corporation')
add('/answers/can-i-still-file-a-t2-after-my-corporation-was-dissolved/',
    'Can I Still File a T2 After My Corporation Was Dissolved?', None,
    'Yes. The final return is due within six months of the dissolution date, and '
    'earlier unfiled years can still be filed. $300.00 plus HST per tax year.',
    'file a t2 after dissolution')

# ---- Family 5, items 831 to 860: tightened replacements --------------------
# These ten currently carry the full 40-to-60-word answer paragraph as the
# description, per line 1166. That runs 250 to 300 characters and truncates.
add('/answers/what-happens-if-i-dont-file-a-nil-t2/',
    "What Happens if I Don't File a Nil T2?", None,
    'The tax year stays open and the CRA can demand the return and assess the '
    'corporation arbitrarily. What follows, and how to close the year.',
    'what happens if i dont file a nil t2')
add('/answers/what-happens-if-i-dont-file-my-t2-for-five-years/',
    "What Happens if I Don't File My T2 for Five Years?", None,
    'All five returns stay outstanding and each one is filed separately. Five '
    'missed year-ends, five returns, $300.00 plus HST per tax year.',
    'what happens if i dont file my t2 for five years')
add('/answers/what-happens-if-i-dont-file-a-t2-before-dissolving-my-corporation/',
    "What Happens if I Don't File a T2 Before Dissolving?",
    None,
    'Dissolution can be held up and the outstanding years remain due. A clearance '
    'certificate cannot be issued while any tax year is open.',
    'file t2 before dissolving corporation')
add('/answers/what-happens-if-i-dont-report-a-dormant-corporation-to-cra/',
    "What Happens if I Don't Report a Dormant Corporation?",
    None,
    'There is no dormancy filing, so the obligation is the annual T2. A dormant '
    'corporation files every year until it is formally dissolved.',
    'report dormant corporation to cra')
add('/answers/what-happens-if-i-dont-respond-to-a-cra-demand-to-file-a-t2/',
    "What Happens if I Ignore a CRA Demand to File a T2?", None,
    'The CRA can assess the corporation arbitrarily without waiting for the '
    "return. Filing the real return replaces that figure with the corporation's.",
    'cra demand to file a t2')
add('/answers/what-happens-if-i-dont-file-a-nil-t2-for-a-numbered-company/',
    "What Happens if I Don't File a Nil T2 for a Numbered Company?",
    "Numbered Company: What if I Don't File a Nil T2?",
    'Nothing changes because the corporation has a number instead of a name. A '
    'numbered company files a T2 like any other, $300.00 plus HST per tax year.',
    'nil t2 for a numbered company')
add('/answers/what-happens-if-i-dont-file-t2-returns-after-my-corporation-is-dissolved/',
    "What Happens if I Don't File T2 Returns After Dissolution?",
    None,
    'The final return is still required and the years before dissolution stay '
    'outstanding. Dissolving does not cancel the returns already missed.',
    't2 returns after corporation dissolved')
add('/answers/do-i-need-to-file-a-t2-if-my-corporation-had-no-activity/',
    'Do I Need to File a T2 if My Corporation Had No Activity?', None,
    'Yes. Every resident corporation files a T2 within six months of its year-end, '
    'every year, until it is dissolved. $300.00 plus HST per tax year.',
    'file t2 corporation no activity')
add('/answers/do-i-need-to-file-a-nil-t2-if-my-corporation-has-no-bank-account/',
    'Do I Need to File a Nil T2 if My Corporation Has No Bank Account?',
    'Do I File a Nil T2 With No Corporate Bank Account?',
    "Yes. The T2 obligation follows the corporation's existence, not its banking. "
    'A return is due within six months of each fiscal year-end.',
    'nil t2 no bank account')
add('/answers/do-i-need-financial-statements-for-a-nil-t2-return/',
    'Do I Need Financial Statements for a Nil T2 Return?', None,
    'No audited statements are needed, but the return still carries GIFI schedules '
    'showing zero. What a nil year reports, and when GIFI is required.',
    'financial statements for a nil t2')

BANNED = ['cheapest', 'lowest price', 'best price', 'unbeatable', 'guarantee',
          'risk-free', 'risk free', 'fastest', 'instant filing', 'no obligation',
          'penalty free', 'penalty-free', 'zero penalty', 'no penalty',
          'authorized', 'authorised', 'cra agent', 'cra approved', 'cra partner',
          'cra endorsed', 'book a call', 'calendly', 'starting from', 'simply',
          'easily', 'such as', ' just ']

fail = []
for url, title, short, desc, kw in ROWS:
    tag = url
    if len(desc) > 155:
        fail.append('%s: description %d chars' % (tag, len(desc)))
    if short and len(short) > 60:
        fail.append('%s: tightened title %d chars' % (tag, len(short)))
    for field, name in ((title, 'title'), (desc, 'description')):
        low = field.lower()
        for b in BANNED:
            if b in low:
                fail.append('%s: banned phrase "%s" in %s' % (tag, b.strip(), name))
        if re.search(r'T183(?!CORP)', field):
            fail.append('%s: bare T183 in %s' % (tag, name))
        if 'including HST' in field:
            fail.append('%s: "including HST" in %s' % (tag, name))
        if any(ord(c) > 127 for c in field):
            fail.append('%s: non-ASCII in %s' % (tag, name))
    if 'penalt' in desc.lower() and re.search(
            r'(no|without|free of|zero)\s+\w*\s*penalt', desc.lower()):
        fail.append('%s: bare penalty claim in description' % tag)

if len({d for _u, _t, _s, d, _k in ROWS}) != len(ROWS):
    fail.append('duplicate descriptions')
if len({t for _u, t, _s, _d, _k in ROWS}) != len(ROWS):
    fail.append('duplicate titles')

if fail:
    print('GATE FAILED')
    for f in fail:
        print(' -', f)
    sys.exit(1)

out = []
out.append('RANK MATH FIELDS -- %d URLs' % len(ROWS))
out.append('Title target 60 chars, description target 155. T = title length, D = description length.')
out.append('')
for url, title, short, desc, kw in ROWS:
    out.append('URL   ' + url)
    flag = '  <-- over 60, tightened option below' if len(title) > 60 else ''
    out.append('T%-3d  %s%s' % (len(title), title, flag))
    if short:
        out.append('T%-3d  %s   (alternative)' % (len(short), short))
    out.append('D%-3d  %s' % (len(desc), desc))
    out.append('KW    ' + kw)
    out.append('')

txt = '\n'.join(out)
open(os.path.join(HERE, 'rank-math-fields.txt'), 'w', encoding='utf-8').write(txt)
print(txt)
