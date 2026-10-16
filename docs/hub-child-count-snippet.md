# Live child count for the Family 16 hubs — WPCode snippet

## Why this exists

Line 1224 makes the child count the publish gate for every hub:

> "No hub publishes without a live child count and links to every child family."
> Unique data block: "Live child count for that family". Source: "WordPress query
> count, cached hourly by LiteSpeed Cache". Note: **"Child counts update
> automatically and are never hand-typed."**

So the number cannot be written into the page. Line 350 intends an Elementor Loop
Grid to render it, but Theme Builder is unproven on this install — the `Single –
Deadline` and `Single – Cost` templates built earlier are still parked because
nothing on this site has ever rendered through Theme Builder. A shortcode does the
same job with no dependency on it.

## Install this before loading /guides/

Until it is registered, `/guides/` renders the literal text
`[cnf_child_count type="nil_guide"]` where the number belongs. That is deliberate: a
visibly missing shortcode is better than a silently stale hand-typed number, which
would breach the gate.

WPCode → Add Snippet → Add Your Custom Code → **PHP Snippet**. Set *Run Everywhere*,
Activate. Unlike the earlier one-off snippets, **this one stays active permanently** —
it is what keeps the count live.

```php
/**
 * Live child count for the Family 16 hub pages.
 * Usage: [cnf_child_count type="nil_guide"]
 * Plan line 1224: counts update automatically and are never hand-typed.
 */
add_shortcode( 'cnf_child_count', function ( $atts ) {

	$atts = shortcode_atts( array( 'type' => 'post' ), $atts, 'cnf_child_count' );
	$type = sanitize_key( $atts['type'] );

	if ( ! post_type_exists( $type ) ) {
		return '0';
	}

	$counts = wp_count_posts( $type );

	return isset( $counts->publish ) ? number_format_i18n( (int) $counts->publish ) : '0';
} );
```

`wp_count_posts()` reads a cached count, and LiteSpeed caches the rendered page on top
of that, which is exactly the "WordPress query count, cached hourly by LiteSpeed Cache"
the plan names as the source.

## Reuse on the other four hubs

The same shortcode serves every Family 16 hub once those are built. Pass the post type:

| Hub | Shortcode |
|---|---|
| `/guides/` | `[cnf_child_count type="nil_guide"]` |
| `/tools/` | `[cnf_child_count type="nil_calculator"]` |
| `/locations/` | `[cnf_child_count type="nil_service_place"]` |
| `/services/` | `[cnf_child_count type="nil_service_place"]` |
| `/blog/` | `[cnf_child_count type="post"]` |

## What is still not automatic

The **count** is live. The **list of guide cards** on `/guides/` is written by
`build/f16/build_f16.py` and must be regenerated when a guide is added. That is
consistent with how every other page on this site is produced — the plan's own model is
a Python pipeline writing content — but it is not the Loop Grid line 350 describes.

If Theme Builder is ever proven on this install, the card list should move to a Loop
Grid and the generator's `GUIDES` list can be deleted. Until then, adding a guide means
re-running the generator and republishing the hub.
