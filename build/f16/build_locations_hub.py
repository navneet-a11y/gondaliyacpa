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
 ('Ontario', 'ontario', 'ontario',
  'Ontario corporations file the T2 federally. The Ontario annual return is '
  'filed separately through the Ontario Business Registry and is not covered '
  'by the fee.'),
 ('British Columbia', 'british-columbia', 'british-columbia',
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
EXTRA = (".ei-plist{columns:2;column-gap:26px;margin:12px 0 0;padding:0 0 0 20px}\n"
         ".ei-plist li{break-inside:avoid;margin:0 0 7px;color:#4a5568;"
         "line-height:1.6}\n"
         ".ei-prov{margin:0 0 26px}\n"
         ".ei-prov:last-child{margin-bottom:0}\n"
         ".ei-prov h3{margin:0 0 4px;font-size:1.15em;font-weight:700;"
         "color:#1a2340}\n"
         ".ei-prov h3 a{color:#1a2340;text-decoration:none}\n"
         ".ei-prov h3 a:hover{color:rgba(32,135,201,1)}\n"
         "@media(max-width:700px){.ei-plist{columns:1}}\n")


def card(href, title, desc):
    return ('<div class="ei-card"><h3><a href="' + href + '">' + title
            + '</a></h3><p>' + desc + '</p></div>')


def province(name, hub_slug, suffix, note):
    items = ''.join(
        '<li><a href="%s/%s/">%s in %s</a></li>'
        % (SITE, slug % suffix, label, name) for label, slug in SERVICES)
    return ('<div class="ei-prov">\n<h3><a href="' + SITE + '/' + hub_slug
            + '/">Nil T2 Filing in ' + name + '</a></h3>\n<p>' + note + '</p>\n'
            '<ul class="ei-plist">' + items + '</ul>\n</div>')


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
             '<p>The T2 is a federal return, so the filing itself does not '
             'change with the province. What changes is the registry filing '
             'that sits beside it, and each province page states that filing '
             'and its deadline.</p>\n'
             + '\n'.join(province(*q) for q in PROVINCES)
             + '\n</div></div>\n')

    p.append('<div class="ei-section-alt"><div class="ei-wrap ei-art">\n'
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
