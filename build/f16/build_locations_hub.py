# -*- coding: utf-8 -*-
"""Family 16 hub: /locations/.

Plan line 1203: the place index, entry keyword "nil t2 filing near me", fed by
Family 3 city hubs and Family 4 service-place URLs, with the note "Only place
index; no city sub-hubs". So this is the single place index and it links down
to the jurisdiction hubs and to every service-place URL.

What is live decides what it links: 24 Family 4 URLs across two provinces, and
zero Family 3 city hubs, so no city section is rendered at all. A hub that
links a family with nothing in it would be a promise the site cannot keep.

Carries the wp:html wrapper from the start, for the reason the tools hub had to
be patched: without it wpautop inserts a stray close tag after the hero
eyebrow, an unclosed paragraph around the CTA and a paragraph around the
JSON-LD. The [cnf_child_count] shortcode still resolves inside the block.
"""
import io, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = 'https://corpnilfilingfor300.ca'
FORM = SITE + '/form/'
TODAY, ISO = 'October 23, 2026', '2026-10-23'
PRICE = '$300.00 plus HST per tax year'
HUB = SITE + '/locations/'
TITLE = 'Nil T2 Filing by Province'
# No "and City" in the title: zero Family 3 city hubs are built, and a
# title cannot promise a section the page does not have.
PAGE_TITLE = 'Nil T2 Filing by Province in Canada'
META = ('Nil T2 filing wherever your corporation is registered. Every province '
        'page and every service we file, at ' + PRICE + '.')

# The twelve Family 4 services, and the slug each province uses for them. Taken
# from the live list rather than composed, because the cost slug carries an
# "in" the other eleven do not.
SERVICES = [
 ('Nil T2 Filing',                       'nil-t2-filing-%s'),
 ('Catch-Up Nil T2 Filing',              'catch-up-nil-t2-filing-%s'),
 ('Dormant Corporation Filing',          'dormant-corporation-filing-%s'),
 ('Final T2 Before Dissolution',         'final-t2-before-dissolution-%s'),
 ('T2 Short Filing',                     't2-short-filing-%s'),
 ('Inactive Holding Corporation T2 Filing',
  'inactive-holding-corporation-t2-filing-%s'),
 ('Nil T2 Filing Cost',                  'nil-t2-filing-cost-in-%s'),
 ('Unfiled Corporate Tax Returns',       'unfiled-corporate-tax-returns-%s'),
 ('No Activity Corporation Tax Return',  'no-activity-corporation-tax-return-%s'),
 ('Numbered Corporation Nil Filing',     'numbered-corporation-nil-filing-%s'),
 ('Nil T2 Filing Deadline',              'nil-t2-filing-deadline-%s'),
 ('Nil T2 Filing for Non-Resident-Owned Corporations',
  'nil-t2-filing-for-non-resident-owned-corporations-%s'),
]

PROVINCES = [
 ('Ontario', 'ontario', 'ontario', 'Registry filing: Ontario annual return',
  'Ontario corporations file the T2 federally. The Ontario annual return is '
  'filed separately through the Ontario Business Registry and is not covered '
  'by the fee.'),
 ('British Columbia', 'british-columbia', 'british-columbia',
  'Registry filing: BC annual report',
  'British Columbia corporate income tax is collected through the federal T2. '
  'The BC annual report is filed separately with BC Registries and Online '
  'Services.'),
]

ALSO = [
 (SITE + '/services/', 'Nil T2 Filing Services',
  'Every service we file, described in full, before you pick a province.'),
 (SITE + '/tools/', 'Tools and Calculators',
  'Deadlines, T2 Short eligibility, GIFI schedules and unfiled years.'),
 (SITE + '/pricing/nil-t2-filing-cost/', 'Nil T2 Filing Cost',
  'What ' + PRICE + ' covers, and what falls outside a nil return.'),
]

CSS = io.open(os.path.join(HERE, 'hub.css'), encoding='utf-8').read()
EXTRA = """
/* Province jump nav, so a thirteen-province index stays navigable. */
.ei-jump{display:flex;flex-wrap:wrap;gap:8px;margin:16px 0 0;padding:0;list-style:none}
.ei-jump a{display:inline-block;background:#f0f7fd;border:1px solid #cfe4f6;border-radius:50px;padding:6px 15px;font-size:.9em;font-weight:600;color:#1a2340;text-decoration:none}
.ei-jump a:hover{background:rgba(32,135,201,1);border-color:rgba(32,135,201,1);color:#fff}
/* Province card: the left accent rule is the service pages' .cnf-lic pattern,
   recoloured to the hub palette so all five hubs still match each other. */
.ei-pcard{background:#fff;border:1px solid #e2e8f0;border-left:4px solid rgba(32,135,201,1);border-radius:10px;padding:20px 22px;margin:18px 0 0;box-shadow:0 4px 14px rgba(26,35,64,.05);scroll-margin-top:90px}
.ei-pcard h3{margin:0 0 8px;font-size:1.18em;font-weight:800;color:#1a2340;line-height:1.3}
.ei-pcard h3 a{color:#1a2340;text-decoration:none}
.ei-pcard h3 a:hover{color:rgba(32,135,201,1)}
.ei-badge{display:inline-block;background:#fff6e6;border:1px solid #f6d79a;border-radius:5px;padding:3px 10px;font-size:.76em;font-weight:700;text-transform:uppercase;letter-spacing:.5px;color:#8a5a00;margin:0 0 10px}
.ei-pgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:0 28px;margin:14px 0 0;padding:0;list-style:none}
.ei-pgrid li{margin:0}
.ei-pgrid a{display:block;padding:7px 0 7px 17px;position:relative;color:#3a4a63;text-decoration:none;font-size:.875em;font-weight:500;line-height:1.45;border-bottom:1px solid #eef2f7;transition:color .12s ease,padding-left .12s ease}
.ei-pgrid a:before{content:"";position:absolute;left:3px;top:50%;width:4px;height:4px;margin-top:-4px;border-right:1.5px solid #7f94ad;border-bottom:1.5px solid #7f94ad;transform:rotate(-45deg);transition:border-color .12s ease}
.ei-pgrid a:hover{color:#1a7ab5;padding-left:21px}
.ei-pgrid a:hover:before{border-color:#1a7ab5}
/* Numbered steps, from the service pages' .cnf-steps. */
.ei-steps{list-style:none;counter-reset:s;display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px;margin:16px 0 0;padding:0}
.ei-steps>li{counter-increment:s;position:relative;background:#fff;border:1px solid #e9eff7;border-radius:12px;padding:18px 18px 18px 60px;color:#4a5568;line-height:1.6;font-size:.96em}
.ei-steps>li:before{content:counter(s);position:absolute;left:16px;top:16px;width:32px;height:32px;border-radius:50%;background:#1a2340;color:#fff;font-weight:800;line-height:32px;text-align:center;font-size:.95em}
.ei-steps>li ul{margin:9px 0 0;padding-left:16px;font-size:.92em}
.ei-steps>li ul li{margin:0 0 4px}
.ei-mid-cta{text-align:center;margin:22px 0 0}
/* Reviewer cards, from the service pages' .cpa-card. */
.ei-cpa{display:grid;grid-template-columns:repeat(auto-fit,minmax(310px,1fr));gap:16px;margin:16px 0 0}
.ei-cpac{display:flex;gap:18px;align-items:center;background:#fff;border:1px solid #e2e8f0;border-radius:14px;padding:18px;box-shadow:0 4px 14px rgba(26,35,64,.05)}
.ei-cpac img{width:118px;height:143px;object-fit:cover;border-radius:10px;flex-shrink:0}
.ei-cpat h3{margin:0 0 3px;font-size:1.08em;font-weight:800;color:#1a2340;line-height:1.3}
.ei-cpat p{margin:0 0 5px;font-size:.9em;line-height:1.5;color:#4a5568}
.ei-cpat .ei-role{color:#1a2340;font-weight:700}
.ei-cpat a{text-decoration:none}
@media(max-width:600px){.ei-cpac{flex-direction:column;text-align:center}.ei-cpac img{width:100%;max-width:210px;height:auto}}
/* FAQ. Visual only: hard rule 6 forbids FAQPage schema. */
.ei-faq{margin:16px 0 0}
.ei-faq details{border:1px solid #e2e8f0;border-radius:10px;background:#fff;margin:0 0 10px}
.ei-faq summary{cursor:pointer;list-style:none;padding:15px 46px 15px 18px;font-weight:700;color:#1a2340;position:relative;line-height:1.45}
.ei-faq summary::-webkit-details-marker{display:none}
.ei-faq summary:after{content:"";position:absolute;right:20px;top:50%;width:8px;height:8px;margin-top:-6px;border-right:2px solid rgba(32,135,201,1);border-bottom:2px solid rgba(32,135,201,1);transform:rotate(45deg);transition:transform .15s ease}
.ei-faq details[open] summary:after{transform:rotate(-135deg);margin-top:-2px}
.ei-faq .ei-a{padding:0 18px 16px;color:#4a5568;line-height:1.75;margin:0}
@media(max-width:700px){.ei-pgrid{grid-template-columns:1fr}}
/* Centred section headers, as the service pages have them, and more air
   between sections. Page-local on purpose: hub.css still left-aligns the
   headings on the other four hubs, so this is the only hub that centres them
   until they are republished too.
   The media query has to be restated here. hub.css sets .ei-art .ei-h2 to
   1.3em inside its own @media, and a media query adds no specificity, so a
   plain rule placed after it would otherwise win at every width and leave
   mobile at the desktop size. */
.ei-art .ei-h2{text-align:center;font-size:1.6em;margin:0 0 14px}
.ei-art .ei-lead{text-align:center;max-width:700px;margin:0 auto 16px}
.ei-section,.ei-section-alt{padding:48px 20px}
.ei-count{display:flex;width:fit-content;margin:0 auto 18px}
.ei-jump{justify-content:center;margin:4px 0 0}
@media(max-width:900px){.ei-art .ei-h2{font-size:1.38em}.ei-section,.ei-section-alt{padding:34px 18px}}
"""


def card(href, title, desc):
    return ('<div class="ei-card"><h3><a href="' + href + '">' + title
            + '</a></h3><p>' + desc + '</p></div>')


def province(name, hub_slug, suffix, badge, note):
    """One province as a card: heading, registry badge, note, link grid.

    Was a bare <ul> in two CSS columns. Thirteen of those stacked is a wall of
    identical blue text with nothing to fix the eye on, which is what looked
    wrong. The card gives each province an edge, the badge surfaces the one
    fact that actually differs between provinces, and the grid rows get a
    divider and a chevron so they read as a list of destinations.
    """
    items = ''.join(
        '<li><a href="%s/%s/">%s in %s</a></li>'
        % (SITE, slug % suffix, label, name) for label, slug in SERVICES)
    return ('<div class="ei-pcard" id="p-' + hub_slug + '">\n'
            '<h3><a href="' + SITE + '/' + hub_slug + '/">Nil T2 Filing in '
            + name + '</a></h3>\n'
            '<span class="ei-badge">' + badge + '</span>\n'
            '<p>' + note + '</p>\n'
            '<ul class="ei-pgrid">' + items + '</ul>\n</div>')


def jump():
    return ('<ul class="ei-jump">'
            + ''.join('<li><a href="#p-%s">%s</a></li>' % (q[1], q[0])
                      for q in PROVINCES)
            + '</ul>')


# Verbatim from the home page, which states these four more plainly than the
# service templates do: no sub-bullets, no payment-method list, no signing
# mechanics. A locations index is a signpost, so the shorter four are the right
# ones. The heading is the home page's too, "(Complete Within 10 Minutes)"
# included, so the same promise is worded the same way in both places.
STEPS_HEADING = 'How It Works, in Four Steps (Complete Within 10 Minutes)'
STEPS = [
 ('Give basic details like your corporation name.', []),
 ('Pay $300.00 plus HST per tax year.', []),
 ('Confirm your tax year dates, shareholder details and the rest of your '
  'filing information.', []),
 ('Sign your Form T183CORP.', []),
]

REVIEWERS = [
 ('sharad-gondaliya-cpa.png', 'Sharad Gondaliya, CPA',
  'https://gondaliyacpa.ca/team/sharad-gondaliya-cpa/',
  'Principal, Registered EFILE Electronic Filer', '647-212-9559'),
 ('vandana-goel-cpa.png', 'Vandana Goel, CPA',
  'https://gondaliyacpa.ca/vandana-goel-cpa/',
  'Accounting Specialist', '647-250-0242'),
]

# Unique to this hub: every question is about province and place, which is what
# someone arriving on a locations index is actually asking. No links out to
# other question pages. Visual accordion only, no FAQPage schema (hard rule 6).
FAQ = [
 ('Does the province my corporation is registered in change the T2 return?',
  'No. The T2 is a federal return filed with the Canada Revenue Agency, and a '
  'nil T2 is prepared the same way wherever the corporation is registered. '
  'What changes is the registry filing that sits beside it, and in some '
  'provinces a separate provincial return. Each province page states which '
  'applies there.'),
 ('Is the provincial annual return included in the fee?',
  'No. $300.00 plus HST per tax year covers the nil T2 return to '
  'CRA. Provincial registry filings are filed separately and are not covered, '
  'including the Ontario annual return through the Ontario Business Registry '
  'and the British Columbia annual report through BC Registries and Online '
  'Services.'),
 ('My corporation is federally incorporated but operates from one province. '
  'Which page applies?',
  'Use the page for the province the corporation is registered or '
  'extra-provincially registered in, because that registration is what decides '
  'the registry filing beside the T2. The federal annual return under the '
  'Canada Business Corporations Act is a separate filing again, and is also '
  'not covered by the fee.'),
 ('Do you file the Quebec CO-17 or the Alberta AT1?',
  'Neither is part of a federal T2 filing. The CO-17 is a separate return '
  'filed with Revenu Quebec and the AT1 is a separate return filed with '
  'Alberta Tax and Revenue Administration, so neither is covered by the fee '
  'for the nil T2.'),
 ('There is no page for my province yet. Can the return still be filed?',
  'Yes. The T2 is federal, so a nil return for a corporation registered in a '
  'province without its own page here is prepared and transmitted the same '
  'way. Province pages are being added over time. Start from the filing form '
  'or from the service you need.'),
 ('Do you have an office in my city?',
  'There is one office, at 55 Queen St E, Suite 1205, Toronto. Filing does '
  'not require a visit to it. Details are given on the form, Form T183CORP '
  'is signed on a secure screen, and the return is prepared, reviewed and '
  'transmitted by Sharad Gondaliya, CPA, a registered EFILE electronic '
  'filer, wherever in Canada the corporation is registered.'),
]


def steps_html():
    out = []
    for text, subs in STEPS:
        sub = ('<ul>' + ''.join('<li>' + x + '</li>' for x in subs) + '</ul>'
               ) if subs else ''
        out.append('<li>' + text + sub + '</li>')
    return '<ol class="ei-steps">' + ''.join(out) + '</ol>'


def reviewers_html():
    out = []
    for img, nm, bio, role, tel in REVIEWERS:
        out.append(
            '<div class="ei-cpac">'
            '<img loading="lazy" width="118" height="143" src="' + SITE
            + '/wp-content/uploads/2026/09/' + img + '" alt="' + nm + '">'
            '<div class="ei-cpat"><h3>' + nm + '</h3>'
            '<p><a href="' + bio + '">Bio</a></p>'
            '<p class="ei-role">' + role + '</p>'
            '<p>' + tel + '</p>'
            '<p><a href="mailto:info@corpnilfilingfor300.ca">'
            'info@corpnilfilingfor300.ca</a></p></div></div>')
    return '<div class="ei-cpa">' + ''.join(out) + '</div>'


def faq_html():
    return ('<div class="ei-faq">' + ''.join(
        '<details><summary>' + q + '</summary><p class="ei-a">' + a
        + '</p></details>' for q, a in FAQ) + '</div>')


def render():
    p = ['<!-- wp:html -->\n<style>\n', CSS, EXTRA, '</style>\n']
    p.append('<div class="ei-hero"><div class="ei-hero-inner">'
             '<span class="ei-hero-eyebrow">Locations</span>'
             '<h1>' + TITLE + '</h1>'
             '<p class="ei-hero-sub">' + META + '</p>'
             '<p class="ei-hero-by">Written and reviewed by Sharad Gondaliya, '
             'CPA (Ontario), CPA Ontario Membership 61040184.</p>'
             '<div class="ei-hero-btns"><a class="ei-btn-blue" href="' + FORM
             + '">Start Nil T2 Filing NOW</a></div></div></div>\n')

    p.append('<div class="ei-section"><div class="ei-wrap ei-art">\n'
             '<h2 class="ei-h2">Every Province Page on This Site</h2>\n'
             '<p class="ei-count">Place pages published: '
             '<b>[cnf_child_count type="nil_service_place"]</b></p>\n'
             '<p class="ei-lead">The T2 is a federal return, so the filing itself does not '
             'change with the province. What changes is the registry filing '
             'that sits beside it, and each province page states that filing '
             'and its deadline.</p>\n'
             + jump() + '\n'
             + '\n'.join(province(*q) for q in PROVINCES)
             + '\n</div></div>\n')

    p.append('<div class="ei-section-alt"><div class="ei-wrap ei-art">\n'
             '<h2 class="ei-h2">' + STEPS_HEADING + '</h2>\n'
             '<p class="ei-lead">The process is the same in every province, because the return '
             'is federal.</p>\n'
             + steps_html()
             + '\n<div class="ei-mid-cta"><a class="ei-btn-blue" href="' + FORM
             + '">Start Nil T2 Filing NOW</a></div>\n</div></div>\n')

    p.append('<div class="ei-section"><div class="ei-wrap ei-art">\n'
             '<h2 class="ei-h2">Who Reviews and Files Your Return</h2>\n'
             '<p class="ei-lead">The same two people handle every province.</p>\n'
             + reviewers_html() + '\n</div></div>\n')

    p.append('<div class="ei-section-alt"><div class="ei-wrap ei-art">\n'
             '<h2 class="ei-h2">Questions About Filing by Province</h2>\n'
             + faq_html() + '\n</div></div>\n')

    p.append('<div class="ei-section"><div class="ei-wrap ei-art">\n'
             '<h2 class="ei-h2">Also on This Site</h2>\n<div class="ei-cards">\n'
             + '\n'.join(card(h, t, d) for h, t, d in ALSO)
             + '\n</div>\n<p class="ei-updated">Last reviewed: ' + TODAY
             + '</p>\n</div></div>\n')

    p.append('<div class="ei-cta-bottom"><div class="ei-wrap">'
             '<h2>Nil T2 Filing, ' + PRICE + '</h2>'
             '<p>Type your corporation name, pick your unfiled years, pay, and '
             'sign Form T183CORP on a secure screen. Your CRA confirmation is '
             'emailed within 3 business days.</p>'
             '<a class="ei-btn-blue" href="' + FORM + '">Start Nil T2 Filing '
             'NOW</a></div></div>\n')

    schema = {"@context": "https://schema.org", "@graph": [
      {"@type": "CollectionPage", "@id": HUB + "#webpage", "url": HUB,
       "name": PAGE_TITLE, "description": META, "inLanguage": "en-CA",
       "dateModified": ISO,
       "author": {"@type": "Person", "name": "Sharad Gondaliya",
                  "honorificSuffix": "CPA",
                  "url": SITE + "/sharad-gondaliya-cpa/"}},
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Nil T2 filing in Canada",
         "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": TITLE, "item": HUB}]}]}
    p.append('<script type="application/ld+json">'
             + json.dumps(schema, ensure_ascii=False)
             + '</script>\n<!-- /wp:html -->')
    return ''.join(p)


if __name__ == '__main__':
    html = render()
    io.open(os.path.join(HERE, 'locations-hub.html'), 'w',
            encoding='utf-8').write(html)
    print('locations-hub.html %d bytes, %d provinces, %d service links'
          % (len(html.encode()), len(PROVINCES),
             len(PROVINCES) * len(SERVICES)))
