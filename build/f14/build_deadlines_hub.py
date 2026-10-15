"""Generates the /deadlines/ pillar page.

The plan gives this page structure but no copy: there is no exemplar row for
/deadlines/ in the 6(a) table, unlike /pricing/nil-t2-filing-cost/ at line 1169.
What it does give, and what is honoured here:

  6(b) line 1202  pillar for F14; "12 month-end pages and 9 date tools link up";
                  conversion path /deadlines/ -> calculator -> /; entry keyword
                  "t2 filing deadline"
  6(g) line 1536  F14: 4 inbound minimum, 20 outbound maximum, anchor rule is a
                  "month plus year-end phrase"
  line 1222       gate: no deadline page publishes without a computed date and
                  the business-day rule sentence; "file late with no
                  consequence" is banned
  7.5 rule 3      F14 is bylined to the reviewing CPA directly
  line 1690       corporate deadlines live only on corpnil; this URL is canonical

Every date is computed by dates.py, never typed (line 2225).

The 10 catch-up year pages are deliberately NOT linked from here. Linking all 23
children plus the money pages would put the page at 25 outbound and break the
20 cap. They hang off /catch-up-nil-t2-filing/ instead, which is already live.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dates import due_date, last_day

MONTHS = ['January','February','March','April','May','June','July','August',
          'September','October','November','December']
SITE = 'https://corpnilfilingfor300.ca'
BYLINE = ('Written and reviewed by Sharad Gondaliya, CPA (Ontario), '
          'CPA Ontario Membership 61040184.')
BUSINESS_DAY = ('Where a due date falls on a Saturday, a Sunday or a public holiday '
                'recognised by the Canada Revenue Agency, a return received the next '
                'business day is on time.')
EFILE = ('We are a registered EFILE electronic filer. Your return is transmitted to '
         'the Canada Revenue Agency electronically.')

CSS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'ontario', 'hero.css')).read() if os.path.exists(
      os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','ontario','hero.css')) else ''


def rows():
    out = []
    for m in range(1, 13):
        d = due_date(2026, m)
        anchor = '%s %d year-end' % (MONTHS[m-1], last_day(2026, m))
        url = '%s/deadlines/t2-due-date-for-%s-year-end/' % (SITE, MONTHS[m-1].lower())
        out.append('<tr><td><a href="%s">%s</a></td><td>%s %d</td></tr>'
                   % (url, anchor, MONTHS[d.month-1], d.day))
    return '\n'.join(out)


if __name__ == '__main__':
    body = rows()
    assert body.count('<tr>') == 12
    assert 'year-end</a>' in body
    open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'deadlines-hub-rows.html'),
         'w').write(body)
    print('12 computed rows written, anchors are month-plus-year-end')
    print(body.split('\n')[0])
    print(body.split('\n')[11])
