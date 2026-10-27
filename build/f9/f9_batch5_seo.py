"""Rank Math meta for guides 18 to 27, validated before it is applied.

Deliberately avoids the word "penalty" in every description. Hard rule 3 says
a penalty claim always carries the full qualification block, and a 160
character description cannot hold it, so the meta says "charge" and the page
body carries the qualified statement.
"""
SEO = {
 't2-filing-deadlines': (
  'T2 Filing Deadlines | Complete Guide for Canada',
  'The six-month rule, how a weekend or statutory holiday moves a due date, '
  'short and first tax years, and the deadlines that run separately.',
  't2 filing deadlines'),
 'zero-activity-corporate-tax-returns': (
  'Zero-Activity Corporate Tax Returns | Guide',
  'What counts as zero activity, the entries that quietly take a year out of '
  'it, and which schedules a zero-activity return still carries.',
  'zero activity corporate tax returns'),
 'corporate-tax-arrears-and-interest': (
  'Corporate Tax Arrears and Interest | Guide',
  'What arrears are, what interest attaches to, why a nil year creates none, '
  'and how an unfiled year manufactures a balance that was never owed.',
  'corporate tax arrears'),
 'winding-up-an-inactive-corporation': (
  'Winding Up an Inactive Corporation | Guide',
  'The order the steps have to happen in, every return due first, the '
  'clearance certificate, closing the accounts and the registry filing.',
  'winding up an inactive corporation'),
 'small-business-corporate-filing': (
  'Small Business Corporate Filing | Canadian Guide',
  'Everything a small Canadian corporation files each year, which of it is tax '
  'and which is registry, and how to tell a nil year from a trading one.',
  'small business corporate filing'),
 'corporate-compliance-calendar': (
  'Corporate Compliance Calendar | Canadian Guide',
  'Every recurring date a Canadian corporation owes, which ones derive from '
  'your year-end, and the shortest calendar a dormant corporation keeps.',
  'corporate compliance calendar'),
 'numbered-company-maintenance': (
  'Numbered Company Maintenance | Canadian Guide',
  'Keeping a numbered company current between returns: the registry, the '
  'registered office, the minute book and the years nobody filed.',
  'numbered company maintenance'),
 'mandatory-t2-electronic-filing': (
  'Mandatory T2 Electronic Filing | Canadian Guide',
  'The rule for tax years starting after 2023, the flat charge for filing on '
  'paper, why a nil return is not exempt, and how transmission works.',
  'mandatory t2 electronic filing'),
 'schedule-50-and-shareholder-reporting': (
  'Schedule 50 and Shareholder Reporting | Nil T2',
  'What Schedule 50 reports, the 10% threshold, what goes in each row, and why '
  'a nil return still files it in full.',
  'schedule 50'),
 'non-resident-owned-corporation-nil-filing': (
  'Non-Resident-Owned Corporation Nil T2 Filing',
  'Why the daily charge is the largest exposure a dormant corporation carries, '
  'who it reaches, and how a nil year is filed from outside Canada.',
  'non-resident-owned corporation'),
}

if __name__ == '__main__':
    import re, sys
    bad = []
    for slug, (t, d, k) in SEO.items():
        if len(t) > 60:
            bad.append('%s: title %d chars' % (slug, len(t)))
        if not 70 <= len(d) <= 160:
            bad.append('%s: description %d chars' % (slug, len(d)))
        for text, where in ((t, 'title'), (d, 'description')):
            if re.search(r'T183(?!CORP)', text):
                bad.append('%s %s: bare T183' % (slug, where))
            if re.search(r'penalt|cheapest|\bbest\b|fastest|guarantee|risk.free',
                         text, re.I):
                bad.append('%s %s: banned wording -> %r' % (slug, where, text))
            if re.search(r'\$\s?300', text):
                bad.append('%s %s: price belongs in the body, not the meta'
                           % (slug, where))
            if 'EFILE' in text:
                bad.append('%s %s: EFILE needs its full approved phrase'
                           % (slug, where))
        if k != k.lower().strip():
            bad.append('%s: focus keyword not lowercase' % slug)
    if len(set(d for _t, d, _k in SEO.values())) != len(SEO):
        bad.append('duplicate description within the batch')
    if len(set(t for t, _d, _k in SEO.values())) != len(SEO):
        bad.append('duplicate title within the batch')
    if bad:
        print('SEO GATE FAILED')
        for b in bad:
            print(' -', b)
        sys.exit(1)
    print('seo gate clear on all %d guides' % len(SEO))
    for slug, (t, d, k) in sorted(SEO.items()):
        print('  %-42s t:%2d d:%3d  %s' % (slug[:42], len(t), len(d), k))
