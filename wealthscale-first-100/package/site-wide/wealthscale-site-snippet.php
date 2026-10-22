<?php
/**
 * WealthScale site snippet v1.0 (October 22, 2026)
 * Add in Code Snippets as ONE snippet: "WealthScale: assets, page layout, reviewer schema".
 * Run snippet everywhere. Requires the files uploaded to /wp-content/uploads/ws/ (see the publishing guide).
 */

if ( ! defined( 'ABSPATH' ) ) { return; }

/* 1. Load the shared widget CSS and JS on every page, plus the Manrope font. */
add_action( 'wp_enqueue_scripts', function () {
	$base = content_url( '/uploads/ws/' );
	$ver  = '1.0.0'; // Change this number every time you upload new widget files, so caches refresh.
	wp_enqueue_style( 'ws-manrope', 'https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&display=swap', array(), null );
	wp_enqueue_style( 'ws-widgets', $base . 'wealthscale-widgets.css', array(), $ver );
	wp_enqueue_script( 'ws-widgets', $base . 'wealthscale-widgets.js', array(), $ver, array( 'in_footer' => true, 'strategy' => 'defer' ) );
}, 20 );

/* 2. Pages carry their own H1 inside the content, so hide the theme's page title on pages (fixes the duplicate H1). */
add_filter( 'generate_show_title', function ( $show ) {
	return is_page() ? false : $show;
} );

/* 3. Full-width pages with no sidebar (removes recent posts, comments and archives widgets from pages). */
add_filter( 'generate_sidebar_layout', function ( $layout ) {
	return is_page() ? 'no-sidebar' : $layout;
} );

/* 4. No comments on pages. */
add_filter( 'comments_open', function ( $open, $post_id ) {
	return ( 'page' === get_post_type( $post_id ) ) ? false : $open;
}, 10, 2 );

/* 5. Rank Math breadcrumbs above page content (not on the home page). */
add_action( 'generate_before_content', function () {
	if ( is_page() && ! is_front_page() && function_exists( 'rank_math_the_breadcrumbs' ) ) {
		echo '<div class="ws-crumbs">';
		rank_math_the_breadcrumbs();
		echo '</div>';
	}
} );

/*
 * 6. Neha's review line. When Neha signs off a page in her Upwork batch, add a custom field to that page:
 *    Name: ws_neha_reviewed_on   Value: 2026-10-31 (her sign-off date, YYYY-MM-DD)
 *    The line "Review of this page scheduled" then becomes "Reviewed on October 31, 2026",
 *    and the schema below adds her to reviewedBy. Never set this field without her written sign-off.
 */
add_filter( 'the_content', function ( $content ) {
	if ( ! is_page() ) { return $content; }
	$d = get_post_meta( get_the_ID(), 'ws_neha_reviewed_on', true );
	if ( ! $d || ! preg_match( '/^\d{4}-\d{2}-\d{2}$/', $d ) ) { return $content; }
	$nice = date_i18n( 'F j, Y', strtotime( $d ) );
	return preg_replace(
		'#<span class="ws-role ws-review-status" data-ws-review="pending">[^<]*</span>#',
		'<span class="ws-role ws-review-status" data-ws-review="done">Reviewed on ' . esc_html( $nice ) . '</span>',
		$content
	);
}, 20 );

/* 7. Schema: Sharad as author with his profile @id; reviewers in reviewedBy; lastReviewed. */
add_filter( 'rank_math/json_ld', function ( $data, $jsonld ) {
	if ( ! is_page() || ! is_array( $data ) ) { return $data; }
	$sharad = array(
		'@type'            => 'Person',
		'@id'              => 'https://wealthscale.ca/about/sharad-gondaliya/#person',
		'name'             => 'Sharad Gondaliya',
		'honorificSuffix'  => 'CPA',
		'url'              => 'https://wealthscale.ca/about/sharad-gondaliya/',
		'sameAs'           => array( 'https://linkedin.com/in/gondaliya2' ),
	);
	$neha = array(
		'@type'           => 'Person',
		'@id'             => 'https://wealthscale.ca/about/neha-gupta/#person',
		'name'            => 'Neha Gupta',
		'honorificSuffix' => 'CFA',
		'jobTitle'        => 'Financial Reviewer',
		'url'             => 'https://wealthscale.ca/about/neha-gupta/',
		'sameAs'          => array( 'https://www.linkedin.com/in/nehaguptacfa1983/', 'https://directory.cfainstitute.org/members/neha-gupta-a3e6c720' ),
	);
	$post_id    = get_the_ID();
	$neha_date  = get_post_meta( $post_id, 'ws_neha_reviewed_on', true );
	$modified   = get_the_modified_date( 'Y-m-d', $post_id );
	$reviewers  = array( $sharad );
	$last       = $modified;
	if ( $neha_date && preg_match( '/^\d{4}-\d{2}-\d{2}$/', $neha_date ) ) {
		$reviewers[] = $neha;
		$last        = max( $modified, $neha_date );
	}
	foreach ( $data as $key => $entity ) {
		if ( ! is_array( $entity ) || empty( $entity['@type'] ) ) { continue; }
		$types = (array) $entity['@type'];
		if ( array_intersect( $types, array( 'Article', 'BlogPosting', 'NewsArticle' ) ) ) {
			$data[ $key ]['author'] = $sharad;
		}
		if ( array_intersect( $types, array( 'WebPage', 'ProfilePage', 'AboutPage', 'ContactPage' ) ) ) {
			$data[ $key ]['reviewedBy']   = $reviewers;
			$data[ $key ]['lastReviewed'] = $last;
		}
	}
	return $data;
}, 99, 2 );
