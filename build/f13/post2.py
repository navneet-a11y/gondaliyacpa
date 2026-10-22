# -*- coding: utf-8 -*-
"""Post 2. Title 14 of Section 7.8.

Penalties are not mentioned anywhere in this post, so the 1590 qualification
sentence is not triggered. The gate enforces that pairing both ways.
"""
from posts import SITE, wrap

SLUG = 'schedule-50-and-the-10-percent-shareholder-rule'
TITLE = 'Schedule 50 and the 10% Shareholder Rule'
DESC = ('Schedule 50 lists every shareholder at 10% or more. Who counts, what each '
        'row records, and why a nil T2 still needs it.')

def a(h, t):
    return '<a href="%s">%s</a>' % (h, t)

B = []
B.append('<p class="cnf-lead">Schedule 50 is needed for any shareholder at 10% or '
         'more. It lists each of those shareholders, their percentage of common and '
         'preferred shares, and their identification number. A nil T2 still needs it '
         'whenever the threshold is met.</p>')

B.append('<h2>Who counts as a 10% shareholder?</h2>')
B.append('<p>Any shareholder holding 10% or more of a class of shares. The test is '
         'ownership of the shares, not involvement in the company. A shareholder who '
         'has never attended a meeting, never been paid and never signed anything '
         'still appears on Schedule 50 if the holding reaches the threshold.</p>')
B.append('<p>The threshold is read per class. A person holding 5% of the common '
         'shares and 40% of the preferred shares is over the threshold and appears, '
         'with both percentages recorded. A person holding 9% of one class and '
         'nothing else does not appear at all.</p>')
B.append('<p>Shareholders can be people or corporations. A numbered holding company '
         'that owns 100% of an operating company is the only Schedule 50 row that '
         'operating company needs.</p>')

B.append('<h2>Does a nil return still need Schedule 50?</h2>')
B.append('<p>Yes. Schedule 50 records who owns the corporation, and ownership does '
         'not switch off because the corporation stopped trading. A dormant company '
         'with two equal shareholders files Schedule 50 with two rows on it, in a '
         'year where every other figure on the return is zero.</p>')
B.append('<p>This is the schedule people most often leave off a nil return, usually '
         'because the return looks empty and the schedule feels like it belongs to a '
         'trading year. It does not. It belongs to the share register.</p>')

B.append('<h2>What does each Schedule 50 row record?</h2>')
B.append('<p>One row per shareholder at or above the threshold. Each row carries the '
         'following.</p>')
B.append('<div class="cnf-check"><ul>'
         '<li>The shareholder&rsquo;s name, as it appears in the share register.</li>'
         '<li>Whether that shareholder is an individual or a corporation.</li>'
         '<li>The identification number: a social insurance number for an individual, '
         'a business number for a corporation, or a trust account number for a '
         'trust.</li>'
         '<li>The percentage of common shares held.</li>'
         '<li>The percentage of preferred shares held.</li>'
         '<li>Whether the shareholder is resident in Canada.</li>'
         '</ul></div>')
B.append('<p>Percentages are recorded as they stood in the tax year the return '
         'covers, not as they stand on the day the return is prepared. For a '
         'catch-up filing across several years, a share transfer part-way through '
         'means two different Schedule 50s across the batch. See '
         + a(SITE + '/catch-up-nil-t2-filing/', 'catch-up nil T2 filing')
         + ' for how the years are handled together.</p>')

B.append('<h2>Which other schedules travel with a nil return?</h2>')
B.append('<p>Schedule 50 is needed for any shareholder at 10% or more. Schedule 24 is '
         'needed on the first return after incorporation. Schedule 8 and loss '
         'continuity must be recorded.</p>')
B.append('<table><thead><tr><th scope="col">Schedule</th>'
         '<th scope="col">Required when</th><th scope="col">Notes</th></tr></thead>'
         '<tbody>'
         '<tr><td>Schedule 50</td><td>Any shareholder at 10% or more</td>'
         '<td>Filed on a nil return as well as a trading one</td></tr>'
         '<tr><td>Schedule 24</td><td>The first return after incorporation</td>'
         '<td>Filed once, on the first return only</td></tr>'
         '<tr><td>Schedule 8 and loss continuity</td><td>Every return</td>'
         '<td>Loss continuity must be recorded even at $0.00</td></tr>'
         '<tr><td>GIFI Schedules 100, 125 and 141</td>'
         '<td>Any share capital, cash, shareholder loan, incorporation cost or bank '
         'charge</td><td>May be omitted only where there is nothing at all to '
         'report</td></tr>'
         '</tbody></table>')
B.append('<p>That last row is the one worth reading twice. A corporation inactive all '
         'year with nothing to report may omit GIFI Schedules 100, 125 and 141, but '
         'any share capital, cash, shareholder loan, incorporation cost or bank '
         'charge makes them required. The '
         + a(SITE + '/guides/gifi-schedules-100-125-141/',
             'guide to GIFI Schedules 100, 125 and 141')
         + ' works through which of those applies, and the '
         + a(SITE + '/guides/schedule-8-and-loss-continuity/',
             'guide to Schedule 8 and loss continuity')
         + ' covers the continuity record.</p>')

B.append('<h2>What happens if Schedule 50 is left off?</h2>')
B.append('<p>The return is incomplete. An incomplete return can be rejected at '
         'transmission, and a rejected return is not a filed return: the year stays '
         'open until a complete return is accepted. Where the omission is found '
         'later, the fix is an amended return for that year, which is work that the '
         'original filing would have avoided.</p>')
B.append('<p>The share register is also the first thing asked for when a corporation '
         'is sold, wound up, or asked to prove who owns it. A run of returns with a '
         'consistent Schedule 50 is the cleanest version of that proof.</p>')

B.append('<h2>Is Schedule 50 included in the fee?</h2>')
B.append('<p>Yes. The fee of $300.00 plus HST per tax year covers one nil T2 return '
         'for one corporation for one tax year, including the T2 Short where the '
         'corporation qualifies, GIFI Schedules 100, 125 and 141 where they are '
         'required, Schedule 24 on a first return, Schedule 50 for every shareholder '
         'at 10% or more, Schedule 8, loss continuity, your Form T183CORP package, '
         'single-use secure e-signing, CPA review, electronic transmission to the '
         'Canada Revenue Agency by a registered EFILE electronic filer, one corrected '
         'transmission if the Canada Revenue Agency rejects the first one, and your '
         'CRA confirmation emailed within 3 business days.</p>')
B.append('<p>No schedule is charged as an extra. You are asked for the shareholder '
         'details once, during '
         + a(SITE + '/nil-t2-filing/', 'nil T2 filing')
         + ', and they are carried into every year in the batch. For a first return '
         'after incorporation, the '
         + a(SITE + '/guides/first-year-t2-filing/', 'first-year T2 filing guide')
         + ' covers Schedule 24 and the 53-week rule alongside it.</p>')
B.append('<p>The whole subject in one place is the '
         + a(SITE + '/guides/nil-t2-return-complete-guide/',
             'complete guide to the nil T2 return') + '.</p>')

HTML = wrap('\n'.join(B), SLUG, TITLE, DESC)
