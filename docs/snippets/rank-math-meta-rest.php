<?php
/**
 * Expose Rank Math's SEO title, meta description and focus keyword to the
 * WordPress REST API.
 *
 * Rank Math stores these as ordinary post meta but does not register them with
 * show_in_rest, so the REST API cannot read or write them. Without this, every
 * page on this site falls back to Rank Math's %excerpt% template for its meta
 * description instead of carrying one written for it, and the SEO title cannot
 * differ from the post title.
 *
 * NOT exposed, deliberately: rank_math_robots. That is the field holding the
 * site-wide noindex that hard rule 10 depends on until Sharad Gondaliya
 * confirms launch. Leaving it unwritable means no automated edit can flip it by
 * accident. Set it in Rank Math by hand, as the decision of 2026-09-21 says.
 *
 * Install: WPCode, Add Snippet, Add Your Custom Code, PHP Snippet.
 * Insert Method: Auto Insert. Location: Run Everywhere. Then Save and Activate.
 * Paste everything BELOW this comment block, without the opening <?php tag if
 * WPCode supplies its own.
 *
 * @package corpnilfilingfor300
 */

add_action(
	'init',
	function () {

		// Every post type this site publishes structural URLs from, plus the
		// two built-in ones. A key has to be registered per post type.
		$post_types = array(
			'post',
			'page',
			'nil_vertical',
			'nil_calculator',
			'nil_city_hub',
			'nil_service_place',
			'nil_question',
			'nil_listicle',
			'nil_comparison',
			'nil_cost',
			'nil_guide',
			'nil_first_filing',
			'nil_review_hub',
			'nil_case_study',
			'nil_deadline',
		);

		$keys = array(
			'rank_math_title'         => 'wp_strip_all_tags',
			'rank_math_description'   => 'wp_strip_all_tags',
			'rank_math_focus_keyword' => 'wp_strip_all_tags',
			'rank_math_canonical_url' => 'esc_url_raw',
		);

		foreach ( $post_types as $post_type ) {
			foreach ( $keys as $key => $sanitizer ) {
				register_post_meta(
					$post_type,
					$key,
					array(
						'type'              => 'string',
						'single'            => true,
						'show_in_rest'      => true,
						'sanitize_callback' => $sanitizer,
						// Only someone who can already edit the post may change
						// its SEO fields. This is the same check wp-admin makes.
						'auth_callback'     => function ( $allowed, $meta_key, $post_id ) {
							return current_user_can( 'edit_post', $post_id );
						},
					)
				);
			}
		}
	},
	// Priority 20, so this runs after Rank Math has registered its own meta on
	// the default priority and this registration is the one that stands.
	20
);
