# MBOT Membership: Status and Paste Blocks

Last update: Tuesday, October 20, 2026. Source: `MBOT-Website-and-Directory-Copy.txt`. All copy below is the exact text from that file.

## What I found on the site (read-only, nothing changed)

- **The Organization/AccountingService node is not from a Rank Math schema template.** Rank Math has 0 schema templates (`rank_math_schema` is empty). The node is written by hand into Elementor HTML widgets:
  - **About page (4026), widget `b2676c7`** (last widget on the page): `"@type": "AccountingService"`, `"@id": "https://gondaliyacpa.ca/#organization"`. This is the node the brief means.
  - **Home page (8), widget `35df112`**: an `@graph` with `#localbusiness` (`["LocalBusiness","AccountingService"]`) and `#organization` (`Organization`).
  - Rank Math also prints its own site-wide Organization node with the same `@id` (`https://gondaliyacpa.ca/#organization`). I could not check the live output: this session cannot reach gondaliyacpa.ca, and the connector's Rank Math tools are switched off.
- Rank Math PRO has **no memberOf field** in its settings. To put memberOf on the Rank Math node, use the filter in `rankmath-memberOf-snippet.php` (WPCode Lite is active).
- Both pages are Elementor pages. The connector can't safely save Elementor data, the same limit as row 17 in the PSB project. So tasks 1 to 3 have to be done in the Elementor editor. The blocks below are ready to paste.
- **Link Whisper Premium is inactive.** Its folder is renamed `link-whisper-premium-off`. It has to be turned back on before task 4.

## Task 1: memberOf schema (Navneet, due Oct 20)

Add this to the existing node, never as a separate node:

```json
"memberOf": {
  "@type": "Organization",
  "name": "Mississauga Board of Trade",
  "url": "https://mbot.com/"
}
```

1. **Rank Math (site-wide):** WPCode > Add Snippet > PHP Snippet. Paste `rankmath-memberOf-snippet.php` (without the opening `<?php` line if WPCode adds it), set it to Run Everywhere, and activate it. The snippet adds memberOf only to the Rank Math node whose `@id` is `https://gondaliyacpa.ca/#organization`.
2. **About page, widget `b2676c7`:** paste the block straight after `"email": "info@gondaliyacpa.ca",`, with the trailing comma shown:
   ```
   "email": "info@gondaliyacpa.ca",
   "memberOf": {
     "@type": "Organization",
     "name": "Mississauga Board of Trade",
     "url": "https://mbot.com/"
   },
   ```
3. **Home page, widget `35df112`:** in the `#organization` node (the second node in `@graph`), paste the same lines after `"email": "info@gondaliyacpa.ca",`. This node has the same `@id`, so it stays one node.
4. Update both pages, clear the LiteSpeed cache, then run the home and About URLs through the Rich Results Test. There should be one `#organization` node, and it should show memberOf.
5. **Astro:** done in this repo. See `astro/schema/organization-memberOf.json`.

## Task 2: Mississauga hub section (Navneet, due Oct 20)

Page 5177, https://gondaliyacpa.ca/mississauga/. Suggested place: straight after the "Official Partner" logo strip (widget `b200519`) and before "How Our Tax Accounting Process Works". Use a new container with 60px top margin and two widgets:

**Heading widget.** Copy the style from "Why Mississauga Corporations Need Professional Corporate Tax Accountant" (`a74ad24`): Poppins 600, 26px, color #2087C9, centered. Use H2.

```
Member of the Mississauga Board of Trade
```

**Text Editor widget** (Text/HTML tab):

```html
<p>Gondaliya CPA Professional Corporation is a member of the <a href="https://mbot.com/">Mississauga Board of Trade</a>. We work with incorporated businesses across Mississauga on corporate tax filing, bookkeeping, payroll and GST/HST, on a fixed flat fee agreed upfront. If you are an MBOT member looking for a CPA for your corporation, please <a href="https://gondaliyacpa.ca/consultation/">book a consultation</a>.</p>
```

## Task 3: About page affiliations block (Navneet, due Oct 20)

Page 4026, https://gondaliyacpa.ca/about-us/. Put it under the "Recognition & Affiliations" heading (`cc0c596`) and above the logo strip (`1659a49`). Add a centered Text Editor widget:

```html
<p style="text-align:center;"><strong>Professional memberships:</strong> CPA Ontario (Firm ID 61330051), Mississauga Board of Trade</p>
```

## Task 4: Link Whisper (14 Mississauga service pages to the hub)

Turn Link Whisper Premium back on first. Then, for target https://gondaliyacpa.ca/mississauga/ (5177), add one inbound link from each of these pages:

| # | ID | URL |
|---|---|---|
| 1 | 36145 | /corporate-tax-filing-mississauga/ |
| 2 | 37777 | /how-to-start-business-in-mississauga/ |
| 3 | 39260 | /gst-hst-filing-mississauga/ |
| 4 | 39655 | /corporate-tax-filing-cost-in-mississauga/ |
| 5 | 39680 | /corporate-tax-planning-mississauga/ |
| 6 | 40351 | /incorporation-services-mississauga/ |
| 7 | 40986 | /cra-audit-resolution-services-in-mississauga/ |
| 8 | 41405 | /cpa-compilation-report-mississauga/ |
| 9 | 41927 | /past-account-cleanup-mississauga/ |
| 10 | 43235 | /catch-up-corporate-tax-filing-mississauga/ |
| 11 | 43695 | /gst-hst-registration-mississauga/ |
| 12 | 44383 | /non-resident-tax-filing-in-mississauga/ |
| 13 | 44896 | /voluntary-disclosure-program-vdp-mississauga/ |
| 14 | 45335 | /payroll-services-mississauga/ |

These are all 14 top-level pages with "Mississauga" in the title. I left out the /reviews/mississauga/ page and the 2 case studies.

## Task 5: Keyword.com

This session has no Keyword.com access. Add these 9 keywords (location Mississauga, ON, Google.ca):

accountant Mississauga, CPA Mississauga, corporate tax accountant Mississauga, T2 corporate tax filing Mississauga, small business accountant Mississauga, bookkeeping Mississauga, payroll services Mississauga, GST HST filing Mississauga, cross-border tax accountant Mississauga

## Task 6: Event recap posts

Ongoing: one post within 2 days of each MBOT event attended, including the monthly Good Morning Mississauga. Send me the event name, date, a few notes and a photo, and I'll build the draft. Link each recap to /mississauga/.

## MBOT directory listing

Section 1 of the copy file. It waits on the MBOT member portal login.
