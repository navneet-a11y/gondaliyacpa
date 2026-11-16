# -*- coding: utf-8 -*-
"""Family 2 batch 15: the Ontario annual return due date calculator.

Navneet, 2026-11-16: "1. /tools/ontario-annual-return-due-date-calculator/ --
closes the 6(e) link set". This is the twelfth and last of the Section 6(e)
"free tools that earn links", and the only one of the twelve not already live.

THE SLUG, AND WHY IT IS NOT THE APPENDIX A ONE
----------------------------------------------
The plan names this tool twice under one slug and once under another:

  6(e), line 1297   /tools/ontario-annual-return-due-date-calculator/
  Outreach, 1642    /tools/ontario-annual-return-due-date-calculator/
  Appendix A, 2928  /ontario-annual-return-deadline-calculator/

Two of the three say due-date, Navneet's instruction says due-date, and line
1642 schedules an outreach push to Ontario small-business media on August 20,
2027 pointing at the due-date URL. An outreach link that 404s is worse than a
slug that disagrees with Appendix A, so due-date wins. Logged in decisions.md.
Appendix A's /ontario-annual-return-deadline-calculator/ is therefore spent,
not merely unbuilt, and so is /ontario-annual-return-requirement-checker/,
which asks the same question this tool answers.

THE INPUT IN 6(e) IS WRONG, AND THE TOOL DOES NOT USE IT
--------------------------------------------------------
Line 1297 gives the input as "Ontario incorporation date". The Ontario annual
return is not due on the incorporation anniversary. It is due within six
months after the end of the corporation's tax year, so this tool takes the
fiscal year-end. Confirmed 2026-11-16 against ontario.ca and corroborated by
Crowe Soberman, Lerners and Miller Thomson; the Province does not hold a
corporation's fiscal year-end on file and so sends no reminder.

6(e) is almost certainly conflating this with the Ontario INITIAL return,
which is due 60 days after incorporation and which Appendix A gives its own
separate tool at /ontario-initial-return-deadline-calculator/ (line 2950,
still unbuilt). That tool is the one that takes the incorporation date. The
6(e) defect is logged in decisions.md rather than carried into the page.

The FEDERAL annual return is a third thing again, due on the incorporation
anniversary, and /tools/federal-annual-return-anniversary-calculator/ is
already live for it. /tools/annual-return-vs-tax-return-checker/ already says
the federal one "turns on the anniversary rather than the fiscal year-end",
so this page agrees with it rather than contradicting it. No live page states
the Ontario due date, so nothing here overwrites an earlier claim.

WHAT IT CORRECTS
----------------
6(e) says the tool "corrects the most common Ontario error". The error is not
arithmetic: the Ontario annual return falls on the SAME DATE as the T2, six
months after the same year-end. The error is that it is a different filing,
made in a different place, and not covered by the fee. The Canada Revenue
Agency stopped accepting it with the T2 on May 15, 2021, and returns due after
October 18, 2021 go through the Ontario Business Registry instead. A
corporation that has not looked at this since then is probably not filing it.
That is what the third question asks and what the result turns on.

THE FEE WORDING
---------------
build_f2.PRICE still reads "$300.00 plus HST per tax year" and is NOT changed
here, because it is the accurate record of what the other 100 live Family 2
tools currently say. Navneet settled the wording on 2026-11-12: HST is named
only in the five HST jurisdictions, and a national tool is not one of them.
This page therefore defines its own PRICE and shadows the import. The other
100 need the same correction in one sweep, which is open work, not this file's
job to half-do. Flagged in decisions.md.
"""
import io, json, os, re as _re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from build_f2 import render, meta, yn, a, SITE, HUB, FORM, TOOL_DISCLAIMER
from build_f2b import tool, date, T, G, COST, CMP
from build_f2f import RBASE

# Shadows build_f2.PRICE. See "THE FEE WORDING" above.
PRICE = '$300.00 plus applicable sales tax per tax year'

TODAY, ISO = 'November 16, 2026', '2026-11-16'

OBR = T + 'ontario-business-registry-filing-checker/'
S546 = T + 'schedule-546-ontario-annual-return-checker/'
MISSED = T + 'ontario-missed-annual-returns-calculator/'
FED = T + 'federal-annual-return-anniversary-calculator/'
VS = T + 'annual-return-vs-tax-return-checker/'
SHIFT = T + 'due-date-weekend-holiday-shift-calculator/'
NEXT = T + 'next-t2-due-date-checker/'

SLUG = 'ontario-annual-return-due-date-calculator'

CLOSE = ('The two filings share a date and nothing else: one is a tax return '
         'transmitted to the Canada Revenue Agency, the other is a corporate '
         'record filed with the Province of Ontario.')


def _tbl(head, rows):
    return ('<table class="ei-tbl"><thead><tr>'
            + ''.join('<th scope="col">%s</th>' % h for h in head)
            + '</tr></thead><tbody>\n'
            + '\n'.join('<tr>' + ''.join('<td>%s</td>' % c for c in r)
                        + '</tr>' for r in rows)
            + '\n</tbody></table>')


JS = RBASE + r"""
var out=document.getElementById('out');
function show(){
  var ye=parse('ye'),ont=pick('ont'),since=pick('since'),h,wait=0;
  if(ye===null||ye===undefined){wait++;}
  if(ont===null){wait++;}
  if(since===null){wait++;}
  if(wait>0){
    out.innerHTML='<p>'+wait+' of the three entries '
     +(wait===1?'is':'are')+' still to come.</p>';return;
  }
  var due=dueDate(ye),t2=dueDate(ye),shift=filingDate(ye);
  if(ont==='n'){
    h='<h3>This is not the return your corporation files</h3>';
    h+='<p>The Ontario annual return is filed by a corporation incorporated '
     +'or continued under Ontario law. A corporation incorporated federally '
     +'files the Corporations Canada annual return instead, and that one '
     +'turns on the incorporation anniversary rather than the year-end, so '
     +'nothing below applies to it.</p>';
    h+='<table class="ei-tbl"><thead><tr><th scope="col">Filing</th>'
     +'<th scope="col">What it turns on</th>'
     +'<th scope="col">Where it goes</th></tr></thead><tbody>'
     +'<tr><td>Ontario annual return</td><td>The fiscal year-end</td>'
     +'<td>Ontario Business Registry</td></tr>'
     +'<tr><td>Federal annual return</td><td>The incorporation anniversary</td>'
     +'<td>Corporations Canada</td></tr>'
     +'<tr><td>Federal T2 return</td><td>The fiscal year-end</td>'
     +'<td>Canada Revenue Agency</td></tr>'
     +'</tbody></table>';
    h+='<p>Your T2 for a year-end of '+fmt(ye)+' is still due '+fmt(t2)
     +'. For the federal annual return, the '
     +'<a href="SITEFED">federal annual return anniversary calculator</a> '
     +'works from the incorporation date.</p>';
    h+='<p>'+DISC_JS+'</p>';
    out.innerHTML=h;return;
  }
  h='<h3>Both are due '+fmt(due)+'</h3>';
  h+='<p>Six months after a year-end of '+fmt(ye)+'. The Ontario annual '
   +'return and the federal T2 fall on the same date, which is the reason '
   +'the Ontario one gets missed: it looks like part of the T2 and it is '
   +'not.</p>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">What is due</th>'
   +'<th scope="col">Date</th><th scope="col">Filed where</th>'
   +'<th scope="col">Covered by the fee</th></tr></thead><tbody>';
  h+='<tr><td>Fiscal year-end</td><td>'+fmt(ye)+'</td>'
   +'<td>Nothing is filed on this date</td><td>Not applicable</td></tr>';
  h+='<tr><td>Ontario annual return</td><td>'+fmt(due)+'</td>'
   +'<td>Ontario Business Registry</td><td>No</td></tr>';
  h+='<tr><td>Federal T2 return</td><td>'+fmt(t2)+'</td>'
   +'<td>Canada Revenue Agency, electronically</td><td>Yes</td></tr>';
  h+='</tbody></table>';
  if(shift.getTime()!==t2.getTime()){
    h+='<p>'+fmt(t2)+' is a '+DAY[t2.getUTCDay()]+' or a public holiday, so '
     +'a T2 transmitted by '+fmt(shift)+' is still on time. That shift is a '
     +'Canada Revenue Agency administrative rule and this site does not '
     +'state one for the Ontario Business Registry, so treat '+fmt(due)
     +' as the Ontario date and see the '
     +'<a href="SITESHIFT">weekend and holiday shift calculator</a>.</p>';
  }
  if(since==='n'){
    h+='<h3>There is probably more than one outstanding</h3>';
    h+='<p>The Canada Revenue Agency stopped accepting the Ontario annual '
     +'return with the T2 on May 15, 2021, and every one due after '
     +'October 18, 2021 goes through the Ontario Business Registry. A '
     +'corporation that has filed none since then has one outstanding for '
     +'each year that has gone by, not just the current one. The '
     +'<a href="SITEMISSED">Ontario missed annual returns calculator</a> '
     +'counts them.</p>';
  }else{
    h+='<p>You have filed at least one through the Ontario Business Registry '
     +'already, so the route is the one you know. '+fmt(due)+' is the next '
     +'one.</p>';
  }
  h+='<p>Nil T2 filing at '+PRICE_JS+' covers the T2 on the last row and '
   +'nothing on the row above it. We tell you the Ontario annual return is '
   +'due; filing it is a Registry transaction we do not make on your '
   +'behalf.</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
""".replace('SITEFED', FED).replace('SITESHIFT', SHIFT) \
   .replace('SITEMISSED', MISSED)


TOOL = dict(
 slug=SLUG,
 title='Ontario Annual Return Due Date Calculator | When It Is Due',
 h1_pre='Ontario Annual Return ', h1_span='Due Date Calculator',
 h1='Ontario Annual Return Due Date Calculator',
 eyebrow='Ontario',
 keyword='ontario annual return due date',
 seo_title='Ontario Annual Return Due Date Calculator',
 seo_desc=('The Ontario annual return is due six months after the fiscal '
           'year-end and is filed through the Ontario Business Registry, not '
           'with the T2.'),
 meta=('The Ontario annual return follows the fiscal year-end, not the '
       'incorporation date, and since October 2021 it is filed through the '
       'Ontario Business Registry.'),
 tags=['Six months after the year-end', 'Not filed with the T2',
       'Ontario Business Registry', 'Not covered by the fee'],
 form=tool('Your Ontario corporation and its fiscal year-end',
           [date('ye', 'The fiscal year-end'),
            yn('ont', 'Incorporated or continued under Ontario law?'),
            yn('since', 'Filed an Ontario annual return since October 2021?')],
           'Enter the fiscal year-end and answer the two questions.'),
 js=None,
 sections=[
  ('the-date', 'The Date Comes From the Year-End',
   '<p>The Ontario annual return is due within six months after the end of '
   'the corporation&rsquo;s tax year. Not six months after incorporation, '
   'and not on the incorporation anniversary. A December 31 year-end makes '
   'it due June 30; a March 31 year-end makes it due September 30.</p>\n'
   '<p>That is the same six months the federal T2 runs on, so for any given '
   'year the two land on the same day. The Province does not hold your '
   'fiscal year-end on file, which is why no reminder arrives and why the '
   'date has to be worked out from the year-end rather than waited for.</p>'),
  ('three-returns', 'Three Returns People Call the Annual Return',
   _tbl(['The filing', 'What the date turns on', 'Filed with'],
        [['Ontario annual return', 'Six months after the fiscal year-end',
          'Ontario Business Registry'],
         ['Federal annual return',
          'The incorporation anniversary, each year',
          'Corporations Canada'],
         ['Federal T2 return', 'Six months after the fiscal year-end',
          'Canada Revenue Agency, electronically']])
   + '\n<p>The middle row is a different filing on a different clock, and the '
   + a(FED, 'federal annual return anniversary calculator')
   + ' handles it. The '
   + a(VS, 'annual return versus tax return checker')
   + ' separates the first row from the third in more detail. This page is '
   'only about the first.</p>'),
  ('where-it-goes', 'Why the Route Changed, and What the Fee Covers',
   '<p>Until 2021 the Ontario annual return travelled with the T2 on '
   'Schedule 546. The Canada Revenue Agency stopped accepting it that way on '
   'May 15, 2021, and every return due after October 18, 2021 is filed '
   'through the Ontario Business Registry instead. The '
   + a(S546, 'Schedule 546 checker')
   + ' covers what happened to the schedule, and the '
   + a(OBR, 'Ontario Business Registry filing checker')
   + ' covers what else goes through the same system.</p>\n'
   '<p>' + a(COST, 'Nil T2 filing at ' + PRICE)
   + ' covers the T2 and not the Ontario annual return. We tell you the date '
   'this page works out, and the Registry filing stays yours to make. If '
   'several years have gone by unfiled, the '
   + a(MISSED, 'Ontario missed annual returns calculator')
   + ' counts how many are outstanding.</p>\n'
   '<p>' + CLOSE + '</p>'),
 ],
 faq=[
  ('When is the Ontario annual return due?',
   'Within six months after the end of the corporation&rsquo;s tax year. A '
   'December 31 year-end makes it due June 30.'),
  ('Is it due on the incorporation anniversary?',
   'No. That is the federal annual return filed with Corporations Canada. '
   'The Ontario one runs from the fiscal year-end.'),
  ('Is it the same date as the T2?',
   'Yes, for the same year-end. Both run six months from the end of the tax '
   'year, which is exactly why the Ontario one is so often missed.'),
  ('Is it filed with the T2?',
   'Not since 2021. The Canada Revenue Agency stopped accepting it on '
   'May 15, 2021, and it goes through the Ontario Business Registry now.'),
  ('Does a nil corporation still file it?',
   'Yes. It is a corporate record filing rather than a tax return, so having '
   'earned nothing in the year does not remove it.'),
  ('Is it included in the fee?',
   'No. The fee covers the federal T2. The Ontario annual return is a '
   'Registry transaction we do not make on your behalf.'),
  ('What happens if it is never filed?',
   'The corporation falls out of compliance with the Province and can '
   'eventually be dissolved by the Ministry for it.'),
  ('What if the due date is a Saturday?',
   'The next-business-day shift is a Canada Revenue Agency administrative '
   'rule for the T2. This site states no such rule for the Registry.'),
  ('My corporation is federal but operates in Ontario.',
   'Then the annual return it files is the federal one on its anniversary. '
   'Extra-provincial registration is a separate question again.'),
  ('How many can be outstanding at once?',
   'One for every year since the last one filed. Nothing caps the number, '
   'and they do not merge into a single catch-up filing.'),
 ],
 related=[
  (OBR, 'Ontario Business Registry filing checker'),
  (MISSED, 'Ontario missed annual returns calculator'),
  (S546, 'Schedule 546 Ontario annual return checker'),
  (FED, 'Federal annual return anniversary calculator'),
  (VS, 'Annual return versus tax return checker'),
  (NEXT, 'Next T2 due date checker'),
 ],
)


def wire(form):
    sel = []
    for tag in _re.findall(r'<input\b[^>]*>', form):
        if 'type="radio"' in tag:
            m = _re.search(r'name="([\w-]+)"', tag)
            if m and 'input[name="%s"]' % m.group(1) not in sel:
                sel.append('input[name="%s"]' % m.group(1))
        else:
            m = _re.search(r'id="([\w-]+)"', tag)
            if m and '#' + m.group(1) not in sel:
                sel.append('#' + m.group(1))
    assert sel, 'the tool form has no input controls'
    return ("\nArray.prototype.forEach.call(\n"
            "  document.querySelectorAll('" + ','.join(sel) + "'),\n"
            "  function(el){el.addEventListener('change',show);"
            "el.addEventListener('input',show);});\nshow();\n")


# RBASE carries PRELUDE, and PRELUDE embeds build_f2.NOT_NIL, which names the
# overflow price as "$350.00 plus HST per year". Same 2026-11-12 correction as
# PRICE above and the same reason: a national tool cannot name HST. Shadowed
# here rather than in build_f2, which still records what the other 100 say.
OVERFLOW_WAS = '$350.00 plus HST per year'
OVERFLOW_NOW = '$350.00 plus applicable sales tax per year'
assert OVERFLOW_WAS in JS, 'the overflow price moved; re-check the shadow'

TOOL['js'] = (JS + wire(TOOL['form'])).replace(OVERFLOW_WAS, OVERFLOW_NOW)

# ---- the contract, as batch 14 states it -------------------------------
_LIVE = {f[:-5] for f in os.listdir(HERE) if f.endswith('.html')}
PUBLISHED = SLUG in _LIVE
assert len(_LIVE - {SLUG}) >= 100, (
    'expected the 100 tools of batches 1 to 14, found %d' % len(_LIVE - {SLUG}))

_PLAN = io.open(os.path.join(HERE, '..', '..', 'docs',
                             'corpnilfilingfor300-seo-website-plan.md'),
                encoding='utf-8').read()
# Appendix A spells this one differently; 6(e) and the outreach calendar are
# the authority here. See the module docstring.
assert '/tools/%s/' % SLUG in _PLAN, '%s is in neither 6(e) nor Appendix A' % SLUG
assert '\n/%s/\n' % SLUG not in _PLAN, (
    'Appendix A now carries this slug too, so the deviation note is stale')

t = TOOL
assert len(t['sections']) == 3 and len(t['faq']) == 10
assert len(t['related']) == 6 and len(t['tags']) == 4
assert sum('<table class="ei-tbl"' in h for _i, _h2, h in t['sections']) >= 1
assert t['js'].count('<table class="ei-tbl"') >= 1
assert len(t['seo_title']) <= 60, len(t['seo_title'])
assert 70 <= len(t['seo_desc']) <= 160, len(t['seo_desc'])

_vars = _re.findall(r'^var ([A-Za-z_]\w*)=', t['js'], _re.M)
assert not {v for v in _vars if _vars.count(v) > 1}, 'PRELUDE applied twice'

_body = ''.join(h for _i, _h2, h in t['sections'])
assert CLOSE in _body

radios, fields = set(), set()
for tag in _re.findall(r'<input\b[^>]*>', t['form']):
    if 'type="radio"' in tag:
        m = _re.search(r'name="([\w-]+)"', tag)
        if m:
            radios.add(m.group(1))
    else:
        m = _re.search(r'id="([\w-]+)"', tag)
        if m:
            fields.add(m.group(1))
for nm in radios:
    assert "'%s'" % nm in t['js'], 'radio %s is never read' % nm
for fid in fields:
    assert "'%s'" % fid in t['js'], 'field %s is never read' % fid
for nm in set(_re.findall(r"pick\('([\w-]+)'\)", t['js'])):
    assert nm in radios, 'js reads radio %s the form lacks' % nm
for fid in set(_re.findall(r"parse\('([\w-]+)'\)", t['js'])):
    assert fid in fields, 'js reads field %s the form lacks' % fid

_all = (t['form'] + _body + ''.join(q + aa for q, aa in t['faq'])
        + ''.join(u2 for u2, _x in t['related']) + t['js'])
for u in _re.findall(r'href="' + SITE + r'/tools/([a-z0-9-]+)/"', _all):
    assert u in _LIVE or u == SLUG, 'links to missing tool %s' % u
_F9 = {f[:-5] for f in os.listdir(os.path.join(HERE, '..', 'f9'))
       if f.endswith('.html')}
for u in _re.findall(r'href="' + SITE + r'/guides/([a-z0-9-]+)/"', _all):
    assert u in _F9, 'links to missing guide %s' % u

# Hard rules. A national tool names no HST and no bare T183.
assert 'plus HST' not in _all and 'including HST' not in _all
assert not _re.search(r'\bT183\b(?!CORP)', _all)
assert 'FAQPage' not in _all and 'aggregateRating' not in _all
_low = _all.lower()
for _w in ('cheapest', 'best price', 'fastest', 'guaranteed', 'risk-free',
           'book a call', 'calendly', 'cra approved', 'cra agent'):
    assert _w not in _low, 'banned phrase "%s"' % _w


if __name__ == '__main__':
    import build_f2
    build_f2.TODAY, build_f2.ISO = TODAY, ISO
    build_f2.PRICE = PRICE          # so render()'s PRICE_JS matches the body
    html, url = render(TOOL)
    assert 'plus HST' not in html, 'the rendered page still names HST'
    io.open(os.path.join(HERE, SLUG + '.html'), 'w',
            encoding='utf-8').write(html)
    rec = dict(slug=SLUG, title=TOOL['title'], url=url, content=html,
               rank_math_title=TOOL['seo_title'],
               rank_math_description=TOOL['seo_desc'],
               rank_math_focus_keyword=TOOL['keyword'], **meta(TOOL))
    json.dump([rec], io.open(os.path.join(HERE, 'f2o-manifest.json'), 'w',
                             encoding='utf-8'), ensure_ascii=False, indent=1)
    print('%-48s %6d bytes' % (SLUG, len(html.encode())))
