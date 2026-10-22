# -*- coding: utf-8 -*-
"""Post 1. Title 5 of Section 7.8."""
from posts import SITE, QUAL, EFILE_RULE, wrap

SLUG = 'mandatory-t2-e-filing-after-2023'
TITLE = 'Mandatory T2 E-Filing for Tax Years Starting After 2023'
DESC = ('Electronic filing is mandatory for virtually all corporations for tax years '
        'starting after 2023, and a paper T2 draws two separate penalties.')

def a(h, t):
    return '<a href="%s">%s</a>' % (h, t)

B = []
B.append('<p class="cnf-lead">For tax years starting after 2023 electronic filing is '
         'mandatory for virtually all corporations. A paper T2 draws a $1,000.00 '
         'penalty plus a $100.00 per-return preparer penalty. A nil return is not '
         'exempt: no activity still means transmit electronically.</p>')

B.append('<h2>What changed for tax years starting after 2023?</h2>')
B.append('<p>' + EFILE_RULE + ' The test is the tax year, not the filing date. A '
         'corporation with a December 31 year-end is inside the rule for its 2024 '
         'year and every year after it, whether that return is filed on time or '
         'years late.</p>')
B.append('<p>The change matters most to the corporations that file least. A company '
         'that trades every day already files electronically through its accountant. '
         'A dormant company whose owner has posted a paper return each year, or has '
         'not filed at all, is the one that meets the rule for the first time.</p>')

B.append('<h2>Does the rule apply to a nil return?</h2>')
B.append('<p>Yes. A nil return is a T2. It is the same return, with zeros in it, and '
         'it carries the same transmission requirement as a return reporting a '
         'million dollars of income. Every resident corporation, including an '
         'inactive one, must file a T2 within six months of its fiscal year-end, '
         'every year, until it is formally dissolved. A final T2 is due within six '
         'months of dissolution.</p>')
B.append('<p>There is no small-corporation exception, no dormancy exception and no '
         'first-year exception. If you are unsure what counts as nil, the '
         + a(SITE + '/guides/nil-t2-return-complete-guide/',
             'complete guide to the nil T2 return') + ' sets out the test.</p>')

B.append('<h2>What does a paper T2 cost?</h2>')
B.append('<p>Two penalties, stated together because they apply together. The first is '
         'charged on the return. The second is charged per return to the preparer.</p>')
B.append('<table><thead><tr><th scope="col">Item</th><th scope="col">Amount</th>'
         '<th scope="col">Notes</th></tr></thead><tbody>'
         '<tr><td>Paper filing penalty</td><td>$1,000.00</td>'
         '<td>Charged per return filed on paper</td></tr>'
         '<tr><td>Preparer penalty</td><td>$100.00</td>'
         '<td>Charged per return to the preparer</td></tr>'
         '<tr><td>Both penalties on one paper return</td><td>$1,100.00</td>'
         '<td>The two figures added</td></tr>'
         '<tr><td>Nil T2 filed electronically through this site</td><td>$300.00</td>'
         '<td>Plus HST, per tax year, CPA reviewed</td></tr>'
         '</tbody></table>')
B.append('<p>Filing one nil year on paper therefore costs more in penalties than '
         'filing three years electronically. See the full '
         + a(SITE + '/pricing/nil-t2-filing-cost/', 'nil T2 filing cost')
         + ' for what the fee covers.</p>')

B.append('<h2>What about the late-filing penalty on a nil year?</h2>')
B.append('<p>The paper penalty and the late-filing penalty are different things, and '
         'they are often confused. The qualification below applies in full and is the '
         'wording this firm uses everywhere.</p>')
B.append('<div class="cnf-qual"><p>' + QUAL + '</p></div>')
B.append('<p>Read that carefully, because it cuts both ways. The percentage penalty is '
         '$0.00 on a true nil year. The paper penalty is not a percentage of anything, '
         'so it is unaffected by the corporation owing nothing.</p>')

B.append('<h2>Who can transmit a T2 electronically?</h2>')
B.append('<p>Transmission is done by a registered EFILE electronic filer. Gondaliya '
         'CPA Professional Corporation is a registered EFILE electronic filer. '
         'Returns are prepared and transmitted in Canada. Credentials are never '
         'shared and never used offshore.</p>')
B.append('<p>Before any return is transmitted you sign Form T183CORP as an authorized '
         'signing officer. The form carries that return&rsquo;s figures, is dated with '
         'a timestamp, and is signed before transmission rather than after. The '
         + a(SITE + '/guides/t183corp-signing-and-transmission/',
             'guide to signing and transmitting Form T183CORP')
         + ' sets out who may sign and what the timestamp is for.</p>')

B.append('<h2>What if the corporation has several unfiled years?</h2>')
B.append('<p>File them oldest year first. A T2 carries forward figures from the year '
         'before it, so the years are assessed in order, and each year is a separate '
         'return at the same fee. Years that fall inside the rule are transmitted '
         'electronically; the order does not change because of it.</p>')
B.append('<div class="cnf-check"><ul>'
         '<li>List every tax year the corporation has not filed, oldest first.</li>'
         '<li>Confirm the corporation had no activity in each of those years.</li>'
         '<li>Check the fiscal year-end against the Canada Revenue Agency record, '
         'because a year-end that does not match gets the transmission rejected.</li>'
         '<li>Sign one Form T183CORP for each year, each carrying that year&rsquo;s '
         'figures.</li>'
         '<li>Keep the CRA confirmation for each year with the corporate records.</li>'
         '</ul></div>')
B.append('<p>If that is your situation, '
         + a(SITE + '/catch-up-nil-t2-filing/', 'catch-up nil T2 filing')
         + ' handles the years together, and '
         + a(SITE + '/deadlines/', 'the deadline pages')
         + ' give the due date for every fiscal year-end.</p>')

B.append('<h2>What the rule does not change</h2>')
B.append('<p>Electronic filing replaces the paper return. It does not replace anything '
         'else the corporation owes. A nil T2 does not cover your provincial annual '
         'return, a federal Corporations Canada annual return at $12.00 due within 60 '
         'days of your anniversary, an Alberta AT1, a Quebec CO-17, or a nil GST/HST '
         'or payroll filing. We tell you which of these you still owe.</p>')
B.append('<p>Nor does it change who the service is for. This service is for a '
         'corporation with no activity in the tax year. A corporation with investment '
         'income, rental income, or dividends paid or received is not nil. If your '
         'corporation is not nil, we move your file to gondaliyacpa.ca at $350.00 plus '
         'HST per tax year and tell you before any further charge.</p>')
B.append('<p>The mechanics of a single filing, start to finish, are in '
         + a(SITE + '/guides/how-to-file-a-nil-t2-return/',
             'how to file a nil T2 return') + '.</p>')

HTML = wrap('\n'.join(B), SLUG, TITLE, DESC)
