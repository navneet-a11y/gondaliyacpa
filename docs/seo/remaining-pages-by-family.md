# Structural pages left, ranked on traffic evidence

Written 2026-11-19. Live counts pulled from the site; targets from Section 8.1
of the plan; ranking evidence from Search Console, 2026-08-20 to 2026-11-18
(683 impressions, 8 clicks).

## Where every family stands

| Family | Plan | Live | Left |
|---|---|---|---|
| F1 Industry and entity verticals | 215 | **0** | **215** |
| F2 Calculators and checkers | 150 | 101 | 49 |
| F3 City hubs | 15 | 4 | 11 |
| F4 Service and place matrix | 336 | 53 | **283** |
| F5 Question pages | 45 | 47 | 0 |
| F6 Best and route listicles | 38 | **0** | 38 |
| F7 Comparison pages | 20 | 21 | 0 |
| F8 Cost and pricing | 15 | 17 | 0 |
| F9 Guides and pillars | 30 | 30 | 0 |
| F10 How-to-start and first-filing | 25 | 26 | 0 |
| F11 Reviews hub and by city | 11 | **0** | 11 |
| F12 Case studies | 15 | **0** | 15 |
| F14 Deadline and date pages | 23 | 23 | 0 |
| F15 + F16 Trust, legal, utility and hubs | 29 | 38 pages | 0 |
| **Structural total** | **968** | **360** | **608** |

Seven families are complete. Everything left sits in six.

The plan's own date for all 968 structural URLs was **Friday, November 13,
2026**. That is six days past. Recorded as a fact for Navneet and Sharad
Gondaliya, not something this file tries to solve.

## 1. F4, service and place matrix. 283 left of 336

**This is the best-ranking family on the site and it is only 16% built.**

Of its 53 live pages, 24 draw impressions and **17 of those sit in the top
ten**:

| Page | Impr | Pos |
|---|---|---|
| `/nil-t2-filing-ontario/` | 1 | **1.0** |
| `/nil-t2-filing-quebec/` | 1 | **1.0** |
| `/dormant-corporation-filing-quebec/` | 1 | **1.0** |
| `/unfiled-corporate-tax-returns-ontario/` | 2 | 1.5 |
| `/no-activity-corporation-tax-return-quebec/` | 3 | 2.0 |
| `/nil-t2-filing-cost-in-alberta/` | 4 | 2.25 |
| `/nil-t2-filing-british-columbia/` | 1 | 3.0 |
| `/nil-t2-filing-alberta/` | 6 | 4.83 (**1 click**) |
| ten more between 5.0 and 10.0 | 56 | - |

75 impressions and one of the site's eight clicks, from a sixth of the family.
Nothing else on the site ranks like this.

### Build order, by CRA T2 corporations per jurisdiction

Source: `docs/seo/cra-t2-jurisdiction-counts.json`, 2023 tax year.

| Jurisdiction | 2023 T2s | 5-yr trend | Slugs live |
|---|---|---|---|
| Saskatchewan | 73,110 | +3.6% | 5 of 12 |
| Manitoba | 69,180 | +11.0% | 0 |
| Nova Scotia | 47,490 | +8.6% | 0 |
| New Brunswick | 34,960 | +5.8% | 0 |
| Newfoundland and Labrador | 17,800 | -9.0% | 0 |
| Prince Edward Island | 9,220 | +13.3% | 0 |
| Yukon | 2,430 | +7.0% | 0 |
| Northwest Territories | 1,590 | -10.2% | 0 |
| Nunavut | 630 | 0.0% | 0 |

Finish Saskatchewan first: 73,110 corporations and the template is already
proven there. Then Manitoba, which is the fastest-growing jurisdiction left.
The three territories are 4,650 corporations between them, so they are a
completeness job, not a traffic job.

That is 103 pages. The remaining 180 are 15 cities multiplied by the 12
service slugs.

### One caveat before building

Two of the twelve service slugs rank badly wherever they are published:

| Slug | Ontario | BC | Alberta |
|---|---|---|---|
| `dormant-corporation-filing-` | 64 | 65 | 47.3 |
| `t2-short-filing-` | 50.7 | - | 62 |

Both target nationally competitive queries (`dormant company tax return` sits
at position 66 to 77, `t2 short return` at 84 to 87). Build them for
completeness, but the family's traffic will come from the other ten slugs.

## 2. F3, city hubs. 11 left of 15

Toronto, Mississauga, Brampton and Ottawa are live. The build is now cheap:
duplicate-and-patch at 44 operations per city rather than a 120 KB import.

Next by federal corporation count: Vaughan 14,862, Markham 13,280, Hamilton
10,168, Richmond Hill 10,128, Oakville 10,060, then Oshawa 4,922, Windsor
4,704 and Guelph 2,512.

**Sequence matters here.** Each hub links all 12 service slugs for its city,
so F3 has to run slightly ahead of the 180 city pages in F4 or those pages
land with no hub above them.

## 3. F1, industry and entity verticals. 215 left of 215

The largest untouched family, and the second largest in the plan. No template
exists yet and no Search Console evidence exists either, because nothing is
live.

The argument for it: the vertical keywords (`nil t2 filing for holding
company`, `dormant holding company tax return`, `nil t2 for numbered company`)
are long-tail service intent, the same shape as F4, which is the family that
works.

The argument for caution: 215 pages is the largest single commitment left, on
zero evidence. **Build the template and publish ten as a test batch**, then
read their positions before committing to the other 205.

Hard rule 8 applies throughout: a holding, rental or investment corporation is
not nil, and every one of those verticals has to say so.

## 4. F2, calculators and checkers. 49 left of 150

Template proven, cheap to produce, low value each. The 101 live calculators
average one to three impressions apiece; the best,
`/tools/carrying-on-business-in-canada-checker/`, has 9 at position 8.4.

These earn their place as internal link targets and as the unique-data asset
the plan requires, not as traffic drivers. Finish them after F4 and F3.

## Lowest priority

| Family | Left | Why it waits |
|---|---|---|
| F6 Best and route listicles | 38 | "Best" framing collides with hard rule 4, and every competitor page needs Sharad Gondaliya's approval before it goes live |
| F12 Case studies | 15 | Negligible search volume; these are trust assets, not traffic |
| F11 Reviews hub and by city | 11 | Hard rule 6 keeps review and aggregateRating schema off and Trustindex snippets off, so they cannot win rich results |

## Recommended order

1. Saskatchewan, the 7 missing F4 slugs
2. Manitoba, 12 F4 slugs
3. Nova Scotia and New Brunswick, 24 F4 slugs
4. F3 city hubs, Vaughan through Oakville
5. F1 vertical template plus a 10-page test batch
6. The remaining Atlantic and territory F4 jurisdictions
7. F2, the last 49 calculators
8. City F4 pages behind their hubs
9. F6, F12, F11
