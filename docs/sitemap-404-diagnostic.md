# Rank Math sitemap 404 — diagnostic and fixes

## Why this needs a snippet

The Claude session cannot reach the site over HTTPS (the sandbox proxy refuses the
CONNECT with a 403), and the `corpnil` connector exposes no option reader and no REST
passthrough. So `blog_public`, the Rank Math module list and the rewrite rules cannot be
read from here. The snippet below reads all of them in one pass and prints the answer in
wp-admin.

It is **read-only**. It changes no setting, and it cannot affect hard rule 10.

## Step 1 — paste this in WPCode and open any admin page

WPCode → Add Snippet → Add Your Custom Code → **PHP Snippet**. Set it to *Run
Everywhere*, Activate, load wp-admin, read the notice, then **deactivate and delete it**.

```php
add_action( 'admin_notices', function () {

	if ( ! current_user_can( 'manage_options' ) ) {
		return;
	}

	$out = array();

	// 1. Is the Sitemap module switched on? A disabled module 404s the index.
	$modules = get_option( 'rank_math_modules', array() );
	$out['Sitemap module on'] = ( is_array( $modules ) && in_array( 'sitemap', $modules, true ) )
		? 'yes'
		: 'NO — switch it on at Rank Math > Dashboard > Modules';
	$out['All Rank Math modules'] = is_array( $modules ) ? implode( ', ', $modules ) : 'option missing';

	// 2. Is the sitemap rewrite rule registered?
	$rules = get_option( 'rewrite_rules', array() );
	$found = false;
	if ( is_array( $rules ) ) {
		foreach ( array_keys( $rules ) as $pattern ) {
			if ( false !== strpos( $pattern, 'sitemap_index' ) ) {
				$found = true;
				break;
			}
		}
	}
	$out['sitemap_index rewrite rule'] = $found
		? 'present'
		: 'MISSING — re-save Settings > Permalinks';

	// 3. A real file on disk shadows the virtual sitemap.
	$out['Static sitemap_index.xml on disk'] = file_exists( ABSPATH . 'sitemap_index.xml' )
		? 'YES — delete it over SFTP'
		: 'no';

	// 4. Caching layer.
	$out['LiteSpeed active'] = defined( 'LSCWP_V' )
		? 'yes — exclude sitemaps from cache'
		: 'no';

	// 5. Reported for completeness. This does NOT by itself 404 the sitemap,
	//    and it must stay as it is while hard rule 10 is in force.
	$out['blog_public (0 = discouraged)'] = (string) get_option( 'blog_public' );

	// 6. Which post types Rank Math is told to include.
	$sitemap = get_option( 'rank-math-options-sitemap', array() );
	foreach ( array( 'nil_deadline', 'nil_cost', 'nil_service_place', 'page', 'post' ) as $pt ) {
		$key = 'pt_' . $pt . '_sitemap';
		$out[ 'In sitemap: ' . $pt ] = isset( $sitemap[ $key ] ) ? $sitemap[ $key ] : 'not set';
	}

	echo '<div class="notice notice-info"><p><strong>Rank Math sitemap diagnostic</strong></p><ul style="list-style:disc;padding-left:20px">';
	foreach ( $out as $label => $value ) {
		echo '<li>' . esc_html( $label ) . ': <code>' . esc_html( $value ) . '</code></li>';
	}
	echo '</ul></div>';
} );
```

## Step 2 — fixes, in the order Rank Math recommends

1. **Re-save permalinks.** Settings → Permalinks → Save Changes, without changing
   anything. This is Rank Math's first-line fix and costs nothing. Rank Math also
   suggests changing "Links Per Sitemap" under Rank Math → Sitemap Settings, saving,
   then re-saving permalinks.

2. **Exclude the sitemap from LiteSpeed.** LiteSpeed Cache → Cache → Excludes → Do Not
   Cache URIs, add:

   ```
   /sitemap_index.xml
   /sitemap
   ```

   Then LiteSpeed → Toolbox → Purge All. This install runs LiteSpeed 7.9.1 and the
   conflict is documented.

3. **Check for a static file.** If the snippet reports one, delete
   `sitemap_index.xml` from the web root over SFTP — a real file shadows the virtual one.

4. **Switch the Sitemap module on** if the snippet says it is off.

## Step 3 — why a CPT is still missing after "Include in Sitemap" is on

Two Rank Math settings decide whether a post type reaches the sitemap, and they live in
different screens. Turning the sitemap one on is not enough if the robots one says
noindex, because Rank Math drops noindexed URLs from its sitemaps.

| Screen | Setting | Effect |
|---|---|---|
| Rank Math > Sitemap Settings > `<post type>` | Include in Sitemap | Creates `<post type>-sitemap.xml` |
| Rank Math > Titles & Meta > `<post type>` | Robots Meta > noindex | Silently removes every URL of that type from the sitemap |

Also remember CPT URLs never appear in `page-sitemap.xml`. Check `sitemap_index.xml`
for a `nil_deadline-sitemap.xml` row.

This snippet reports both settings for all three project CPTs at once. Same WPCode
instructions as above, and it is equally read-only.

```php
add_action( 'admin_notices', function () {

	if ( ! current_user_can( 'manage_options' ) ) {
		return;
	}

	$sitemap = get_option( 'rank-math-options-sitemap', array() );
	$titles  = get_option( 'rank-math-options-titles', array() );
	$types   = array( 'page', 'post', 'nil_deadline', 'nil_cost', 'nil_service_place' );

	echo '<div class="notice notice-info"><p><strong>Rank Math per-post-type sitemap state</strong></p>';
	echo '<table class="widefat striped" style="max-width:860px"><thead><tr>'
		. '<th>Post type</th><th>Published</th><th>In sitemap</th>'
		. '<th>Custom robots</th><th>Robots value</th><th>Verdict</th></tr></thead><tbody>';

	foreach ( $types as $pt ) {

		if ( ! post_type_exists( $pt ) ) {
			continue;
		}

		$in_sitemap = isset( $sitemap[ 'pt_' . $pt . '_sitemap' ] ) ? $sitemap[ 'pt_' . $pt . '_sitemap' ] : 'not set';
		$custom     = isset( $titles[ 'pt_' . $pt . '_custom_robots' ] ) ? $titles[ 'pt_' . $pt . '_custom_robots' ] : 'not set';
		$robots     = isset( $titles[ 'pt_' . $pt . '_robots' ] ) ? $titles[ 'pt_' . $pt . '_robots' ] : array();
		$robots     = is_array( $robots ) ? implode( ', ', $robots ) : (string) $robots;

		$noindexed = ( 'on' === $custom && false !== strpos( $robots, 'noindex' ) );

		if ( 'on' !== $in_sitemap ) {
			$verdict = 'EXCLUDED - Include in Sitemap is off';
		} elseif ( $noindexed ) {
			$verdict = 'EXCLUDED - post type is noindex, which beats the sitemap toggle';
		} else {
			$verdict = 'should appear';
		}

		$counts = wp_count_posts( $pt );

		echo '<tr><td><code>' . esc_html( $pt ) . '</code></td>'
			. '<td>' . esc_html( isset( $counts->publish ) ? $counts->publish : 0 ) . '</td>'
			. '<td>' . esc_html( $in_sitemap ) . '</td>'
			. '<td>' . esc_html( $custom ) . '</td>'
			. '<td>' . esc_html( $robots ? $robots : 'none' ) . '</td>'
			. '<td><strong>' . esc_html( $verdict ) . '</strong></td></tr>';
	}

	echo '</tbody></table></div>';
} );
```

Expected published counts right now: `nil_deadline` 23, `nil_service_place` 6,
`nil_cost` 1. If a row says "should appear" but the URLs are still absent from
`sitemap_index.xml`, the cause is the sitemap cache — re-save Sitemap Settings and purge
LiteSpeed.

### If a CPT turns out to be noindexed

Do not simply switch the noindex off to get the sitemap populated. Hard rule 10 keeps
the whole site noindexed until Sharad Gondaliya confirms launch, so the correct end
state before launch is **noindex on, and the URLs therefore absent from the sitemap**.
An incomplete sitemap during the build is expected and harmless; what matters is that
every post type flips together at launch. If the three CPTs are noindexed and pages are
not, that inconsistency is the real finding and belongs in the Friday update.

### Sources for the noindex/sitemap interaction

- Rank Math, *URL not in sitemap* — https://rankmath.com/kb/url-not-in-sitemap/
- Rank Math developer docs, `rank_math/sitemap/exclude_post_type` overrides the Include
  in Sitemap option — https://rankmath.com/docs/filters-and-hooks/admin/sitemap
- WordPress.org support, noindex in the Rank Math meta box removes a page from the
  sitemap — https://wordpress.org/support/?p=14194956

## Specific to this project

Once the index loads, confirm the Family 14 URLs are actually in it. The 23
`nil_deadline` items and page 799 should appear. If `nil_deadline` shows "not set" or
"off" in the snippet output, enable it at Rank Math → Sitemap Settings → Post Types.

Note the plan's own inconsistency here, already logged: line 315 names a
`nil_cost-sitemap.xml`, but the sitemap inventory at line 1308 lists only
"F8 15, F15 24, F16 5, home 1" inside `page-sitemap.xml` and carries no cost sitemap
row at all. Worth settling with Sharad Gondaliya before the sitemap is submitted
anywhere.

## What must not be done

Hard rule 10 keeps the site noindexed until Sharad Gondaliya confirms launch, and the
live decision in CLAUDE.md says to set that in Rank Math and **never** to guard it with
`Disallow: /` in robots.txt. So:

- do not "fix" a sitemap problem by editing robots.txt;
- do not change Settings → Reading to chase this. A disabled `blog_public` is not a
  documented cause of a sitemap 404, and changing it is the one action here that could
  expose a half-built site.

## Sources

- Rank Math, *Why the Sitemap_Index.xml is Throwing a 404 Error* — https://rankmath.com/kb/sitemap-404-error/
- Rank Math, *Rank Math Sitemap Issues and Their Fixes* — https://rankmath.com/kb/fix-sitemap-issues/
