# Change 2: Publishing gate (in force from Thursday, October 29, 2026)

## Hold

**No new pages of these kinds until changes 34 and 35 are done:**
- niche industry
- city × service
- calculator
- Best/Top

The PSB pages and the 10 remaining tax-change drafts carry on, under the rules below.

## Every new URL needs all of these before it is published

1. **A mapped search query.** One primary keyword and up to 4 secondary keywords, recorded in the keyword map (change 27) and in Rank Math.
2. **A unique-content check against its sibling pages.** Run a text-similarity check against the closest 3 pages of the same type, and log the result. Anything above about 50% shared body text gets rewritten or isn't published.
3. **The change 15 byline.** "Written and reviewed by Sharad Gondaliya, CPA", the date of the last review, the /team/sharad-gondaliya-cpa/ link, "CPA Firm License — #61330051" (as it appears on the profile page) and the /editorial-policy/ link.
4. **Sharad's CPA review.** For a tax page, the approval date is recorded.
5. **Pending Review first.** It's created in WordPress with status `pending` (never `publish` directly), author Sharad Gondaliya. It's published the day Sharad approves.
6. **The site rules:**
   - Toronto address and 647-212-9559 only.
   - Only the two trust lines: "1,450+ five-star Google reviews" and "50+ Years Combined Experience".
   - Fees before tax, with HST on its own line.
   - No SR&ED claims, no review or other assurance work, and no personal tax except for owners of corporate clients.
   - No AggregateRating or Review schema about the firm.
7. **Logged.** A row in `CHANGE-LOG.csv`. Any 301 goes in `astro/redirects.csv`.

## Gate check record (one line per new URL)

| Date | URL | Mapped query | Similarity check | Byline | CPA approved | Published |
|---|---|---|---|---|---|---|
