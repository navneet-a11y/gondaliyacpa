# Change 1: Security update checklist

Owner: Navneet. This has to be done in Hostinger hPanel and wp-admin, because it needs staging, wp-config and file access I don't have. Tick each line and send it back, and I'll log it.

## Facts I checked through the API (October 29)

- **WordPress installed: 6.8.11, not 7.0.x.** The update to 7.1.3 is a jump of two major versions, so test carefully on staging. Contact Form 7 6.2.3 already refuses to install until WordPress 7.1.
- **Plugins with an update waiting:**
  - Rank Math PRO: 3.0.98 → 3.0.124
  - Elementor Pro: 4.2.2 → 4.3.2
  - Site Kit: 1.189.0 → 1.190.0
  - UpdraftPlus: 2.26.12.0 → 2.26.14.0
  - Members: 3.2.26 → 3.3.0
  - ElementsKit Lite: 4.0.8 → 4.0.9
  - Easy MCP AI: 2.2.1 → 2.3.1
  - Contact Form 7: 6.1.7 → 6.2.3, which needs WordPress 7.1 first. **This is an 8th plugin not on the plan's list of 7.**
- **Link Whisper Premium 4.0.5 sits in a folder named `link-whisper-premium-off`** (inactive). Delete that folder. Change 25 installs a fresh copy from the vendor.
- I couldn't list themes (the theme tools are switched off), so the "5 unused inactive themes" count isn't confirmed.

## Steps

1. [ ] **UpdraftPlus backup** (database, plugins, themes, uploads, others), stored off-site. Note the backup time.
2. [ ] **Create a staging copy** in Hostinger hPanel › WordPress › Staging.
3. [ ] **Delete the 5 unused inactive themes on staging.** Keep Astra and Twenty Twenty-Five.
4. [ ] **Update WordPress core to 7.1.3 on staging.**
5. [ ] **Update the 7 plugins on staging, plus Contact Form 7,** then the remaining themes.
6. [ ] **Test 10 key pages on staging:**
   - Home
   - /about-us/
   - /contact-us/
   - /pricing-calculation/ (the calculator works)
   - /corporate-tax-return-filing/
   - /tax-preparation-filing/
   - /ei-premium-rates-2026-employer-employee-guide/
   - /toronto/
   - /team/sharad-gondaliya-cpa/
   - one blog post

   On each, check that the header and footer load, the forms submit, the Elementor layout is intact, the Trustindex widget shows, and there are no PHP errors.
7. [ ] **Push staging to live.** Purge LiteSpeed. Repeat the 10-page check on live.
8. [ ] **Rotate the salts:** new keys from https://api.wordpress.org/secret-key/1.1/salt/ into wp-config.php. This logs everyone out.
9. [ ] **Rotate every admin password.** Check Users for any administrator you don't recognize.
10. [ ] **Turn off the debug log in wp-config.php:**
    - `define('WP_DEBUG', false);`
    - `define('WP_DEBUG_LOG', false);`
    - `define('WP_DEBUG_DISPLAY', false);`

    Then delete `/wp-content/debug.log`, and any custom-path log file, through File Manager. Confirm that https://gondaliyacpa.ca/wp-content/debug.log returns 404.
11. [ ] **Run a Wordfence full scan** (Wordfence › Scan › Start new scan). Send me the results.
12. [ ] **In Search Console, check Security & Manual actions:** both Security issues and Manual actions. Send me a screenshot.
13. [ ] **Reconnect the Easy MCP AI connection** if the plugin update changes the key, and check the Search Console source (change 17).

The change log gets one row per step, with the date, the time and who did it.
