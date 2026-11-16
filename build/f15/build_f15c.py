# -*- coding: utf-8 -*-
"""Family 15: /t183corp-signing-explained/.

Navneet, 2026-11-16: "do these /t183corp-signing-explained/ -- 590/mo, one
page, ask Sharad today".

WHAT THE PLAN ASKS FOR
----------------------
Line 1176 fixes the title, the meta description and the H1:
  title  T183CORP Signing Explained | Secure E-Signature
  H1     How T183CORP Signing Works
  note   Never shortens T183CORP to T183
Line 1280 gives it to Family 15 as an informational page on the head term
"t183corp" at an estimated 590 monthly searches, with the conversion path
"Trust page to /security/ to /".
Line 1687 makes it the canonical explanation of T183CORP across the group:
gondaliyacpa.ca's /t183corp-signing/ 301s here.

/security/ IS NOT BUILT, SO THE MIDDLE OF THAT PATH IS MISSING
--------------------------------------------------------------
Checked against the live page list on 2026-11-16. Of the 24 Family 15 slugs
in 6(a), /security/, /identity-verification/, /our-cpas/ and
/cpa-ontario-registration/ are all still unbuilt, and /security/ is the one
this page is supposed to hand off to. Rather than link a 404 or invent the
page's claims, this page carries the handful of safeguards it can state from
what is already published -- the single-use link, the access-controlled
screen, the timestamp, the six-year retention, the Canadian preparation and
transmission -- and ends on the form. When /security/ is built, the third
paragraph of "Where the Signed Form Is Kept" is where it links from. Logged
in decisions.md.

HOW THIS DIFFERS FROM THE GUIDE, AND WHY THAT MATTERS
-----------------------------------------------------
/guides/t183corp-signing-and-transmission/ is live and 21.8 KB, and its H2s
already cover the rules end to end: what the form is, who may sign, when,
the timestamp, e-signature, six-year retention, that it is not sent to the
Agency, EFILE transmission, that it is not a representative authorization,
mandatory electronic filing, rejections, and the fee.

A second page restating those is exactly what 6(k) exists to catch, so this
one takes the other half of the subject: not what the rule is, but what
happens on your screen and what protects it. It is ordered by the signer's
experience -- when the link arrives, what the screen is, what the signature
records, where the form goes afterwards, and what signing does not hand over
-- and it sends the rules to the guide rather than repeating them. It is
measured against the guide at the bottom of this file rather than asserted
here, because the first draft of this docstring guessed the figure.

The hard rule in line 1176 is enforced by build_f15b's gate, which already
fails on a bare T183 not followed by CORP.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import build_f15b
from build_f15b import shell, CSS, FEE, FEE_TITLE, QUAL, a, SITE, FORM

# shell() reads TODAY and ISO from build_f15b's namespace at call time, so a
# page built later than that module's batch would otherwise ship its date.
# The first build of this page shipped "Last reviewed: November 12, 2026".
TODAY, ISO = 'November 16, 2026', '2026-11-16'
build_f15b.TODAY, build_f15b.ISO = TODAY, ISO

GUIDE = SITE + '/guides/t183corp-signing-and-transmission/'
EFILE_GUIDE = SITE + '/guides/mandatory-t2-electronic-filing/'
ESIGN = SITE + '/answers/can-i-e-sign-a-t183corp/'
SIGREQ = SITE + '/tools/t183corp-signature-requirement-checker/'
RETAIN = SITE + '/tools/t183corp-retention-expiry-calculator/'
MULTI = SITE + '/tools/multi-year-signing-requirement-checker/'
HOW = SITE + '/how-it-works/'

SLUG = 't183corp-signing-explained'
URL = SITE + '/' + SLUG + '/'


def page():
    b = []
    b.append('<h2>What You Are Being Asked to Sign</h2>')
    b.append('<p>Form T183CORP is the authorization that lets a CPA transmit '
             'your corporation&rsquo;s T2 to the Canada Revenue Agency '
             'electronically. It is not the return. It is the piece that says '
             'the return is yours, that you have seen it, and that someone '
             'entitled to speak for the corporation says it may go.</p>')
    b.append('<p>Because it carries that return&rsquo;s own figures, it cannot '
             'exist before the return does, and it cannot be signed in '
             'advance. That single fact decides the whole order of what '
             'follows. For the rules behind the form rather than the '
             'experience of signing it, the '
             + a(GUIDE, 'guide to T183CORP signing and transmission')
             + ' sets them out in full.</p>')

    b.append('<h2>Where Signing Sits in the Sequence</h2>')
    b.append('<p>Signing is the eighth of the ten steps on '
             + a(HOW, 'how nil T2 filing works')
             + '. Everything before it exists to make the form accurate, and '
             'everything after it depends on the form being signed.</p>')
    b.append('<ol class="cnf-steps">')
    for s in ['You pay, and we prepare the return from the years you chose.',
              'A CPA reviews it, and Form T183CORP is generated from the '
              'reviewed figures.',
              'A single-use signing link reaches you by email.',
              'You open it and sign on an access-controlled screen.',
              'The signature is recorded with its date and time.',
              'Only then is the return transmitted.']:
        b.append('<li>' + s + '</li>')
    b.append('</ol>')
    b.append('<p class="cnf-cap">Nothing is transmitted before the signature '
             'exists. If you never open the link, the return sits unfiled and '
             'nothing is sent to the Canada Revenue Agency in your '
             'name.</p>')

    b.append('<h2>The Link, and the Screen It Opens</h2>')
    b.append('<p>The link is single-use. It is addressed to you, it opens one '
             'signing screen for one set of returns, and it stops working '
             'once it has been used. There is no portal to register for, no '
             'password to invent and no account left behind afterwards.</p>')
    b.append('<p>The screen itself is access-controlled, which is the reason '
             'the form is never sent to you as a plain email attachment to '
             'print, sign and send back. An attachment can be forwarded, '
             'copied and signed by anyone holding it. A controlled screen '
             'reached by a single-use link can be tied to one signer and one '
             'moment.</p>')

    b.append('<h2>What Your Signature Records</h2>')
    b.append('<p>The signature is stored with the date it was made and the '
             'time to the second, in hours, minutes and seconds. That '
             'timestamp is not decoration. It is what shows the form was '
             'signed before the return was transmitted rather than afterwards, '
             'and it is the detail an electronic signature has to carry for '
             'the form to stand up later.</p>')
    b.append('<p>You do not have to do anything to produce it, and you cannot '
             'set it yourself. It is taken when you sign. The '
             + a(SIGREQ, 'T183CORP signature requirement checker')
             + ' works through whether a given year needs a signature at all, '
             'and the ' + a(ESIGN, 'answer on e-signing Form T183CORP')
             + ' covers the short version of this question.</p>')

    b.append('<h2>Who Has to Be the One Signing</h2>')
    b.append('<p>The signer has to be an authorized signing officer of the '
             'corporation: a director or an officer entitled to bind it. Not '
             'a bookkeeper, not a shareholder who holds no office, and not '
             'us. We prepare the return and we transmit it, and the '
             'authorization to do so has to come from the corporation '
             'itself.</p>')
    b.append('<p>Where several unfiled years are being filed together, each '
             'year is its own return and carries its own Form T183CORP, so '
             'there is a signature for each. They are presented together on '
             'the same screen rather than one link per year. The '
             + a(MULTI, 'multi-year signing requirement checker')
             + ' shows how many a given catch-up involves.</p>')

    b.append('<h2>Where the Signed Form Is Kept</h2>')
    b.append('<p>The signed form is kept for six years. That retention is a '
             'requirement on the filing, not a preference of ours, and the '
             + a(RETAIN, 'T183CORP retention expiry calculator')
             + ' works out the date a particular year&rsquo;s form may be '
             'disposed of.</p>')
    b.append('<p>It is not sent to the Canada Revenue Agency with the return. '
             'The Agency can ask for it, which is the reason it is kept at '
             'all, but it is not part of what is transmitted. The '
             + a(EFILE_GUIDE, 'guide to mandatory electronic filing')
             + ' covers what transmission does involve.</p>')
    b.append('<p>Your return is prepared and transmitted in Canada. Our '
             'credentials are never shared and no part of your file is sent '
             'offshore. We are a registered EFILE electronic filer.</p>')

    b.append('<h2>What Signing Does Not Hand Over</h2>')
    b.append('<div class="cnf-box"><p>Form T183CORP authorizes one '
             'transmission of one return. It is not a representative '
             'authorization: it does not add us to your CRA account, it does '
             'not let us view your corporation&rsquo;s tax information, and it '
             'does not continue into next year. A separate authorization '
             'would be needed for any of that, and this service does not ask '
             'for one.</p>'
             '<p>So the form you sign is narrower than most people expect. It '
             'covers the years in front of you and nothing else.</p></div>')

    b.append('<h2>If the Link Will Not Open</h2>')
    b.append('<p>A single-use link that has already been used will not open a '
             'second time, and this is the commonest reason one appears '
             'broken. Reply to the email it came in and a fresh link is '
             'issued to the same address. Nothing is re-prepared and nothing '
             'is charged again, because the return itself is unchanged.</p>')
    b.append('<p>If the wrong person received the link, do not sign. The '
             'signature has to be the signing officer&rsquo;s own. Tell us and '
             'the link is reissued to the right address.</p>')

    b.append('<h2>What It Costs</h2>')
    b.append('<p>' + FEE + '. Signing is part of the filing and carries no '
             'separate charge, and neither does a reissued link. Each tax '
             'year is a separate return with its own Form T183CORP and its '
             'own fee. See the ' + a(SITE + '/pricing/', 'price')
             + ', or start on ' + a(HOW, 'how nil T2 filing works')
             + '.</p>')

    return shell(
      'How T183CORP Signing Works', FEE_TITLE, 'T183CORP signing explained',
      b, URL,
      'T183CORP Signing Explained',
      'Form T183CORP must be signed by an authorized signing officer before '
      'transmission, carries a date and HH:MM:SS timestamp, and is kept for '
      'six years.',
      't183corp')


PAGE = dict(
  slug=SLUG, title='T183CORP Signing Explained', build=page,
  excerpt='What happens when you sign Form T183CORP: the single-use link, '
          'the timestamp, and the six-year retention.',
  rm_title='T183CORP Signing Explained | Secure E-Signature',
  rm_desc='Form T183CORP must be signed by an authorized signing officer '
          'before transmission, carries a date and HH:MM:SS timestamp, and is '
          'kept for six years.',
  keyword='t183corp',
)


if __name__ == '__main__':
    import re as _re
    from build_f15b import meta
    p = PAGE
    c = p['build']()
    assert len(p['rm_title']) <= 60, (len(p['rm_title']), p['rm_title'])
    assert len(p['rm_desc']) <= 160, len(p['rm_desc'])
    _style = _re.search(r'(?s)<style>(.*?)</style>', c).group(1)
    _body = _re.sub(r'(?s)<style>.*?</style>', '', c)
    _used = set()
    for _v in _re.findall(r'class="([a-z0-9 \-]+)"', _body):
        _used.update(_v.split())
    _def = set(_re.findall(r'\.([a-z][a-z0-9\-]*)', _style))
    _miss = sorted(x for x in _used if x.startswith('cnf') and x not in _def)
    assert not _miss, 'class used with no CSS rule: %s' % _miss
    assert 'HST' not in c.replace('GST/HST', ''), 'names HST'
    assert not _re.search(r'\bT183\b(?!CORP)', c), 'bare T183 (line 1176)'
    assert 'FAQPage' not in c and 'HowTo' not in c and 'aggregateRating' not in c
    _low = c.lower().replace('authorized signing officer', '')
    for _w in ('authorized', 'cra approved', 'cra agent', 'cra partner',
               'cheapest', 'best price', 'fastest', 'guaranteed', 'risk-free',
               'book a call', 'calendly'):
        assert _w not in _low, 'banned "%s"' % _w
    if 'penalt' in c.lower():
        assert QUAL in c, 'penalty without the 7.4 block'
    assert c.count('<h1>') == 1
    # /security/ is not built. Linking it would ship a 404.
    for _dead in ('/security/', '/identity-verification/', '/our-cpas/',
                  '/cpa-ontario-registration/', '/signing-link-expired/'):
        assert _dead not in c, 'links the unbuilt page %s' % _dead
    # 6(k), re-derived rather than remembered. The pairing that matters is
    # this page against the Family 9 guide on the same form; /how-it-works/ is
    # checked too because both narrate the same ten steps.
    import difflib as _dl, glob as _gl

    def _txt(h):
        h = _re.sub(r'(?s)<style.*?</style>', ' ', h)
        h = _re.sub(r'(?s)<script.*?</script>', ' ', h)
        return ' '.join(_re.sub(r'<[^>]+>', ' ', h).split())

    def _ratio(x, y):
        wx, wy = x.split(), y.split()
        return max(_dl.SequenceMatcher(None, wx, wy, autojunk=False).ratio(),
                   _dl.SequenceMatcher(None, wy, wx, autojunk=False).ratio())

    _me = _txt(c)
    _against = ([os.path.join(HERE, '..', 'f9',
                              't183corp-signing-and-transmission.html')]
                + sorted(f for f in _gl.glob(os.path.join(HERE, '*.html'))
                         if not f.endswith(SLUG + '.html')))
    _worst = (0.0, None)
    for _f in _against:
        _r = _ratio(_me, _txt(io.open(_f, encoding='utf-8').read()))
        _worst = max(_worst, (_r, os.path.basename(_f)))
        if 't183corp-signing-and-transmission' in _f:
            _guide = _r
    assert _worst[0] < 0.60, '6(k): %.3f against %s' % _worst
    print('6(k) worst %.3f (%s); against the F9 guide %.3f'
          % (_worst[0], _worst[1], _guide))

    assert 'Last reviewed: ' + TODAY in c, 'the review date did not follow'
    assert '"dateModified": "' + ISO + '"' in c, 'dateModified did not follow'
    io.open(os.path.join(HERE, SLUG + '.html'), 'w', encoding='utf-8').write(c)
    print('%-28s %6d bytes   rm_title %d   rm_desc %d'
          % (SLUG, len(c.encode()), len(p['rm_title']), len(p['rm_desc'])))
