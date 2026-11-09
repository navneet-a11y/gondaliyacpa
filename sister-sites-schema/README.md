# Task 18: Organization schema on the sister sites

Adds `parentOrganization` (Gondaliya CPA Professional Corporation, with `sameAs` https://gondaliyacpa.ca/) to the Organization node Rank Math prints on every page of:

- opencorporationfor35.ca
- corpnilfilingfor300.ca

The connector cannot create WPCode snippets, so this is pasted in by hand. Rank Math has no parentOrganization field.

## Install (each site, about 3 minutes)

1. wp-admin, Code Snippets, Add Snippet, Add Your Custom Code (New Snippet).
2. Title: `Schema - parentOrganization Gondaliya CPA`. Code Type: PHP Snippet.
3. Paste `organization-parent-snippet.php` without the first `<?php` line.
4. Insertion: Auto Insert, Location: Run Everywhere. Set to Active, then Save.
5. Open any page, view source, find `rank-math-schema`, and check that `parentOrganization` shows inside the `#organization` node.
6. Run the home page and the pricing page through https://validator.schema.org/

## Known overlap

129 posts on opencorporationfor35.ca and 9 on corpnilfilingfor300.ca also carry an Organization block written into the post, with parentOrganization but no sameAs and no @id. Those pages show two Organization nodes. Cleaning them up is a separate, batched post edit that needs approval first (more than 20 posts).
