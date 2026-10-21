# Corporate Tax Filing page: changes for the live page

Page: https://gondaliyacpa.ca/tax-preparation-filing/ (WordPress page 1379, built with Elementor)

Open the page with **Edit with Elementor** and make these changes, one at a time. Press **Update** after each one. Elementor keeps a revision of every Update, so any step can be undone from **History → Revisions**.

Not changed, on purpose: the Xero award wording ("Finalist"), the "until 9 PM" line, the page's styles and the new code's top intro box.

---

## Step 1: Top banner (hero)

**Heading** (the big title at the top). Replace "Corporate Tax Filing Services in Toronto" with:

```
Corporate Tax Filing Services in Ontario
```

**Text under it.** Replace "Professional, cost-effective T2 corporate tax return filing by licensed CPAs..." with:

```
A corporation does not file one return a year. It files a set of them, each with its own deadline and its own CRA program account. The T2 is due six months after year-end, and GST/HST returns follow your reporting period. Payroll remittances run all year, and T4 and T5 slips are due by the end of February. The Ontario annual return is due within six months after year-end, and the owners' personal returns by April 30. When two filings report different figures for the same item, CRA can ask the corporation to explain why. Our corporate tax filing services prepare the filings in your engagement from one set of year-end books.
```

---

## Step 2: Industries section: add "Industry-Specific CPA Handling"

Find the heading **"Industries We Serve With Our Corporate Tax Filing Services"**. Drag a **Text Editor** widget directly under that heading and paste:

```
<p><strong>Industry-Specific CPA Handling.</strong> Your corporate tax filing file is matched with a team member who has worked with businesses in your industry, whether you run a dental or medical practice, restaurant, construction company, e-commerce store, trucking company, real estate holding company or consulting firm. Industry details such as revenue streams, HST treatment, payroll structure and equipment classes are handled by someone who knows them. A CPA reviews your corporate tax filing work before anything is filed with CRA or sent to your bank.</p>
```

(Paste it in the Text Editor's **Code/Text** tab, not the Visual tab.) To match the other text on the page, set Style → Typography to Lato, 16px, with text colour #636363.

---

## Step 3: The 14 numbered sections, plus "What We Need From You" and "What You Receive"

Directly under the **"View All Industries"** button, add a new full-width container. Put an **HTML** widget in it and paste the entire contents of `02-html-widget-sections.html`.

That one widget contains, in order:
1. Corporate Filing Deadlines (with the dates table)
2. Year-End Bookkeeping Close
3. Year-End Financial Statements
4. Matching the T2 to Your GST/HST, T4 and T5 Filings
5. GST/HST Returns and Year-End Reconciliation
6. Payroll Year-End
7. Dividends, T5 Slips and Shareholder Records
   - the "Not sure which of these filings…" consultation box
8. Contractor Slips: T4A and T5018
9. Ontario Filings
10. Owners' Personal Returns
11. Tax Instalments and Payment Planning
12. My Business Account, Authorization and CRA Letters
13. Switching Accountants
14. Late or Missed Corporate Filings and Penalties
- What We Need From You / What You Receive (two panels side by side)

The `<style>` block at the top of that file styles only these new sections. Every rule starts with `.gcf`, so nothing else on the page changes.

---

## Step 4: FAQ: replace the 10 questions with the new ones

In the **"Frequently Asked Corporate Tax Filing Questions"** accordion, overwrite the 10 items in order. Put each **Q** in the item's title and each **A** in the Text Editor inside that item. Keep the section heading as it is.

**1. Q:** What filings does an Ontario corporation have to make each year?
**A:** At a minimum, a T2 corporate income tax return and an Ontario annual return on the Ontario Business Registry. A corporation registered for GST/HST also files GST/HST returns, and one that pays salaries remits source deductions through the year and files T4 slips by the end of February. Dividends paid require T5 slips, contractor payments may require T4A or T5018 slips, and an Ontario payroll above the exemption brings Employer Health Tax. The owners' personal returns follow on April 30.

**2. Q:** Is corporate tax filing the same as filing a T2?
**A:** No. The T2 is the corporate income tax return, but it is one of several filings a corporation makes. Our corporate tax filing engagement covers the T2, GST/HST returns, and payroll, dividend and contractor slips, plus year-end financial statements where included, and we check that the Ontario annual return has been filed. If you only need the T2 itself, our Corporate Tax Return Filing (T2) page explains that service schedule by schedule.

**3. Q:** How much does corporate tax filing cost?
**A:** We work on fixed flat fees for business clients, set before the work starts. Our online pricing calculator works out the fee for your corporation from the details you enter, and your engagement letter lists exactly which returns, slips and statements that fee covers. If a filing you need is not listed, ask us before you sign, so the fee and the scope match.

**4. Q:** Can you file my corporation's taxes and my personal taxes together?
**A:** Yes, for owners of the corporations we serve, where included in your engagement letter. Your T4 and T5 slips are checked against the corporate books before your personal return relies on them. Salary, dividends, the shareholder account and any taxable benefits are then reported the same way on both returns. Personal returns are due April 30 for owners paid only salary and dividends.

**5. Q:** Does my corporation need to file GST/HST returns if sales are under $30,000?
**A:** Not while it is unregistered and remains a small supplier, meaning its taxable supplies, including those of its associates, are $30,000 or less in a single calendar quarter and over the last four consecutive calendar quarters. Once a corporation is registered, voluntarily or not, it must file a return for every reporting period, even a nil return, until the registration is cancelled. Whether to register or cancel is handled by our GST/HST registration service.

**6. Q:** When are T4 and T5 slips due?
**A:** T4, T4A and T5 slips and their summaries are due by the last day of February after the calendar year, which for 2026 slips is Monday, March 1, 2027 because February 28 is a Sunday. Copies must reach employees, contractors and shareholders by the same date. A corporation filing more than five slips of one type must file them electronically. T5018 slips for construction subcontractors are different: they are due six months after the end of the chosen reporting period.

**7. Q:** How long does a corporation have to keep its tax records?
**A:** Generally six years from the end of the last tax year the records relate to, under subsection 230(4) of the Income Tax Act, or six years from the filing date when a return is filed late. GST/HST records follow the same six-year rule under section 286 of the Excise Tax Act, and payroll records must be kept for at least six years. Electronic records must stay readable, and destroying records early needs CRA permission.

**8. Q:** Can I switch accountants in the middle of the year?
**A:** Yes. We start from your last filed financial statements, T2 and notice of assessment, and confirm what has already been filed for the current year, such as GST/HST returns and payroll remittances. You authorize us in My Business Account or by confirming our Represent a Client request. Switching before year-end is easier than switching between year-end and the T2 deadline, because the close can be planned from the start. If you plan to switch, book a consultation before your year-end.

**9. Q:** Does an inactive corporation still have to file GST/HST, payroll and Ontario returns?
**A:** Yes, and the T2 is only one of them. An inactive corporation still files a T2 every year and an Ontario annual return on the Ontario Business Registry. If it remains registered for GST/HST, a return is still due for each reporting period, even with nothing to report. A payroll account it no longer uses should be closed, and closing the program accounts it no longer needs ends their filing obligations.

**10. Q:** What documents do I need to send for year-end?
**A:** Send the bank and credit card statements for every corporate account and give us access to your accounting software. Add your sales and purchase invoices, the GST/HST returns filed during the year, payroll registers and remittance confirmations, and contractor details. Include loan statements, investment slips and the minute book records for any dividends or share changes. The full list is in the What We Need From You section above.

---

## Step 5: Price: from $400 to from $300

In the **Pricing** section's Text Editor, change both lines:
- `Tax Preparation (Corporation): From $400` → `Tax Preparation (Corporation): From $300`
- `Tax Return Filing (Corporation): From $400` → `Tax Return Filing (Corporation): From $300`

In the HTML widget below it (the fee comparison table, "Corporate Tax Filing Fees: Gondaliya CPA vs Industry Average"):
- `From $400` → `From $300`
- `$800+` → `$900+` (industry average $1,200 minus $300)

---

## After the last step

Press **Update**. Then go to Elementor → Tools → **Regenerate CSS & Data**, then LiteSpeed Cache → **Purge All**.
