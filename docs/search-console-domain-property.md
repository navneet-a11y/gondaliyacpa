# Search Console: add a Domain property by DNS TXT, keep the URL-prefix property

Neither half of this can be done from the Claude session. The connector exposes no
Google or DNS tools, the sandbox has no DNS resolver (`dig` and `nslookup` are absent,
`gethostbyname` fails), and DNS-over-HTTPS is refused by the proxy. So the TXT record
cannot even be checked for propagation from here. Everything below is done in a browser
and in Hostinger hPanel.

## The one thing that can break something

The root domain already carries TXT records for **SPF, DKIM and DMARC** (plan line 292,
`DMARC p=quarantine`). A domain can hold many TXT records, and the Google verification
string must be added as a **new, separate TXT record**.

Do **not** edit, append to, or overwrite the existing SPF record. Overwriting it breaks
outbound email for the domain, which includes `info@corpnilfilingfor300.ca` and every
CRA-confirmation email the service sends. This is the only destructive mistake available
in this task, and it is easy to make because both records sit at `@` with type TXT.

## Step 1 — create the Domain property

1. Go to https://search.google.com/search-console and open the property picker.
2. Choose **Add property** > **Domain** (the left-hand box), not URL prefix.
3. Enter `corpnilfilingfor300.ca` — no `https://`, no `www`, no trailing slash.
4. Google shows a TXT value of the form `google-site-verification=<random string>`.
   Copy it whole. Leave the dialog open; the Verify button is needed in step 3.

A Domain property covers every subdomain and both protocols at once: `https` and `http`,
`www` and bare, and any future subdomain. That is why it is worth having in addition to
the URL-prefix property, which only ever covers one exact origin.

## Step 2 — add the TXT record in Hostinger

hPanel > **Domains** > `corpnilfilingfor300.ca` > **DNS / Nameservers** > Manage DNS
records.

| Field | Value |
|---|---|
| Type | `TXT` |
| Name | `@` (some panels want this blank — `@` means the root domain) |
| Value / Content | `google-site-verification=<the string from step 1>` |
| TTL | `300` if offered, otherwise leave the default |

Add it as a new record. Confirm afterwards that the SPF record (the TXT starting
`v=spf1`) and the DMARC record (`_dmarc`, starting `v=DMARC1`) are both still present
and unchanged.

## Step 3 — verify

Wait a few minutes for propagation, then click **Verify** in the Search Console dialog.
If it fails, wait longer rather than changing anything — a TTL of 14400 means up to four
hours. Re-check the record in hPanel before touching the Google side.

## Step 4 — keep the URL-prefix property

Do not delete it and do not remove whatever verifies it (an HTML meta tag, an uploaded
file, or a Google account method). The two properties verify independently, so adding
the DNS TXT does not affect the existing one.

Reasons to keep it: its historical performance data stays attached to it, and any
integration already pointed at it keeps working.

## Step 5 — submit the sitemap to the Domain property

Sitemaps are submitted per property, so the new Domain property has none. Submit:

```
https://corpnilfilingfor300.ca/sitemap_index.xml
```

**Expect Google to report the URLs as "Excluded by 'noindex' tag".** That is correct and
is not a fault to chase. Hard rule 10 keeps the whole site noindexed until Sharad
Gondaliya confirms launch, and plan line 1362 states the indexed-count targets apply
only "once Sharad Gondaliya closes the launch gates and the noindex is lifted".
Submitting now simply gets the property ready and gives early crawl diagnostics.

Never use DNS, robots.txt or sitemap settings to manage indexing state. The live
decision in CLAUDE.md is explicit that the noindex lives in Rank Math and is never
guarded with `Disallow: /`.

## Deviation from the plan, for the Friday update

Plan line 1345 sets the launch-gate item as:

> Site Kit by Google: Search Console and Analytics verified, sitemap submitted

**Site Kit by Google is not installed.** The 18 active plugins do not include it. Two
consequences:

1. Verifying by DNS TXT satisfies the Search Console half of that line without Site Kit,
   and is a stronger method — Site Kit normally verifies a URL-prefix property, while
   DNS TXT gives the Domain property. Doing it this way also avoids adding a plugin,
   which CLAUDE.md says needs approval before going live for any tool not already in the
   stack.
2. The **Analytics** half of line 1345 is still unmet, and Site Kit is how the plan
   expects it to be met. Installing Site Kit therefore needs Sharad Gondaliya's approval
   first, or the line needs rewording to allow a different method.

Worth putting both points to him rather than quietly installing the plugin.
