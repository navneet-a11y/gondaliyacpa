# Manual Steps for Navneet

These are the steps the WordPress connector can't do. The exact values per URL are in `build/drafts-table.md`.

## Before Sharad's review on Tue Oct 13

1. **Preview check (2 minutes).** Open the draft preview for page 1 (ID 57063) and page 7 (57088). Check three things:
   - Only one H1 shows. If the theme also prints the page title, turn off the title in Astra for these 20 URLs, the same way the existing accountant-for-* pages do.
   - The Trustindex widget loads.
   - The calculator works on mobile.
2. **Rank Math, all 20 drafts.** The connector can't write Rank Math fields. In each draft's Rank Math panel:
   - Focus keyword, SEO title and meta description: copy them from `build/drafts-table.md`.
   - Page 1 (57063) only: Advanced, then Pillar Content: ON.
   - Schema: the JSON-LD is already inline in the page content, the same way existing pages carry their FAQ schema. Set Rank Math Schema to **None / Off** for these 20 URLs, so each URL has one Service or Article node and one FAQPage.
   - Breadcrumbs stay on. After publishing, view the page source. If Rank Math also outputs a BreadcrumbList, tell me and I'll remove the inline one.
3. **Table CSS (optional).** The gridline CSS is already inline on every draft, so the tables show both gridlines today. Adding it once in Astra, Customize, Custom CSS (package file `07-table-gridlines.css`) is harmless.

## Existing page fix that needs the Elementor editor

4. **Row 17, /team/sharad-gondaliya-cpa/ (ID 25185).** Open it in Elementor and find the widget that holds the Organization schema. Change `"postalCode": "M5H 4C9"` to `"postalCode": "M5C 1R6"` (it appears 4 times in the Elementor data). Update, then clear the LiteSpeed cache.

## Wed Oct 14 (after the pages go live)

5. **Rank Math Redirections:** 301 from `/personal-services-business-tax-calculator/` to `/psb-tax-cost-calculator/`. Then move page 53131 to **Draft**. Do not delete it. It is already on the Astro list (`astro/redirects.csv`).
6. **Make.com:** run "GSC Submit URL & Triple Check" for the 10 page URLs and log pass 3.
7. **llms.txt:** add the heading and the 10 page lines from `package/06-llms-txt-entries.txt`. Add the post lines on Oct 16 (posts 1-5) and Oct 20 (posts 6-10).
8. **Link Whisper:**
   - The 104 planned links are already in the copy.
   - Add inbound links from existing pages, links only, no wording changes. Goal: at least 5 inbound links per new URL and 0 broken links.
   - Rule 8: I can add the one link from /software-development-it-consultants/ to /accountant-for-it-contractors/ once page 2 is live. Just tell me.

## Oct 16 and Oct 20

9. **Short.io:** one link per URL.
10. **Blog2Social:** schedule each post's LinkedIn text (at the end of each post file in `package/04-Posts/`) with its Short.io link. Posts 1-5: Mon Oct 19 to Fri Oct 23. Posts 6-10: Mon Oct 26 to Fri Oct 30. One per weekday.
11. **Featured images:** posts need two-line headline images. The headlines are in each post brief in `package/04-Posts/`. I can make these if you want.

## Later

12. **Keyword.com:** "PSB Contractors" project, 40 keywords (SEO strategy 5.6), Google.ca, Toronto, desktop and mobile.
13. **HubSpot and Calendly (by Oct 21):**
    - Add a "Source page" hidden field to the consultation form.
    - Create the list "PSB cluster consultations".
    - Pass the referring path to Calendly as utm_content.
    - Test from 3 new URLs.
