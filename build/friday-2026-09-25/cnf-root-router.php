<?php
/**
 * cnf-root-router — corpnilfilingfor300.ca
 *
 * WPCode Lite snippet. PHP Snippet, Run Everywhere, priority 10.
 *
 * Three post types live at the site root with no prefix:
 *   nil_vertical (215)   nil_city_hub (15)   nil_service_place (336)
 *
 * WordPress cannot give three post types an empty rewrite slug: each registers
 * its own catch-all rule, the first registered wins every single-segment
 * request, and a slug belonging to either of the other two 404s. So all three
 * are registered in CPT UI with rewrite = false and this snippet owns their
 * URLs instead.
 *
 *   1. post_type_link gives each item its root permalink
 *   2. ONE catch-all rule, injected immediately before WordPress's page rule,
 *      so core rules (REST, feeds, sitemaps) and the ten folder post types all
 *      match first, and real pages keep working
 *   3. the request filter resolves the slug in a single indexed query
 *   4. 566 reserved slugs cannot be taken by a page or post
 *   5. rewrite rules flush once per version, never on every page load
 *
 * The F3 and F4 slugs are generated from their matrices rather than listed,
 * so they cannot drift from the source data. Only F1's 215 are irregular.
 */

if ( ! defined( 'ABSPATH' ) ) { exit; }

define( 'CNF_ROUTER_VERSION', '1.1.0' );

function cnf_root_types() {
	return array( 'nil_vertical', 'nil_city_hub', 'nil_service_place' );
}

function cnf_cities() {
	return array(
		'toronto', 'mississauga', 'brampton', 'scarborough', 'etobicoke',
		'north-york', 'markham', 'vaughan', 'richmond-hill', 'oakville',
		'ottawa', 'oshawa', 'guelph', 'hamilton', 'windsor',
	);
}

function cnf_jurisdictions() {
	return array(
		'ontario', 'quebec', 'british-columbia', 'alberta', 'manitoba',
		'saskatchewan', 'nova-scotia', 'new-brunswick',
		'newfoundland-and-labrador', 'prince-edward-island', 'yukon',
		'northwest-territories', 'nunavut',
	);
}

/** The 12 Family 4 service patterns. %s is one place term. */
function cnf_service_patterns() {
	return array(
		'nil-t2-filing-%s',
		'catch-up-nil-t2-filing-%s',
		'dormant-corporation-filing-%s',
		'final-t2-before-dissolution-%s',
		't2-short-filing-%s',
		'nil-t2-filing-cost-in-%s',
		'unfiled-corporate-tax-returns-%s',
		'no-activity-corporation-tax-return-%s',
		'numbered-corporation-nil-filing-%s',
		'inactive-holding-corporation-t2-filing-%s',
		'nil-t2-filing-deadline-%s',
		'nil-t2-filing-for-non-resident-owned-corporations-%s',
	);
}

/** Family 1, 215 irregular slugs. */
function cnf_f1_slugs() {
	return array(
		'nil-t2-return-for-dormant-consulting-corporations', 'nil-t2-return-for-real-estate-numbered-corporations', 'nil-t2-return-for-trucking-corporations', 'nil-t2-return-for-dental-professional-corporations',
		'nil-t2-return-for-shell-corporations', 'nil-t2-return-for-landscaping-corporations', 'nil-t2-return-for-medical-professional-corporations', 'nil-t2-return-for-it-consulting-corporations',
		'nil-t2-return-for-staffing-agency-corporations', 'nil-t2-return-for-restaurant-corporations', 'nil-t2-return-for-hair-salon-corporations', 'nil-t2-return-for-gym-corporations',
		'nil-t2-return-for-daycare-corporations', 'nil-t2-return-for-ecommerce-corporations', 'nil-t2-return-for-amazon-fba-corporations', 'nil-t2-return-for-crypto-trading-corporations',
		'nil-t2-return-for-photography-corporations', 'nil-t2-return-for-taxi-corporations', 'nil-t2-return-for-moving-corporations', 'nil-t2-return-for-cleaning-corporations',
		'nil-t2-return-for-hvac-corporations', 'nil-t2-return-for-plumbing-corporations', 'nil-t2-return-for-electrical-contracting-corporations', 'nil-t2-return-for-roofing-corporations',
		'nil-t2-return-for-flooring-corporations', 'nil-t2-return-for-painting-corporations', 'nil-t2-return-for-drywall-corporations', 'nil-t2-return-for-welding-corporations',
		'nil-t2-return-for-machine-shop-corporations', 'nil-t2-return-for-printing-corporations', 'nil-t2-return-for-signage-corporations', 'nil-t2-return-for-tutoring-corporations',
		'nil-t2-return-for-translation-corporations', 'nil-t2-return-for-travel-agency-corporations', 'nil-t2-return-for-event-planning-corporations', 'nil-t2-return-for-catering-corporations',
		'nil-t2-return-for-food-truck-corporations', 'nil-t2-return-for-bakery-corporations', 'nil-t2-return-for-brewery-corporations', 'nil-t2-return-for-franchise-corporations',
		'nil-t2-return-for-import-corporations', 'nil-t2-return-for-export-corporations', 'nil-t2-return-for-wholesale-corporations', 'nil-t2-return-for-pharmacy-corporations',
		'nil-t2-return-for-physiotherapy-corporations', 'nil-t2-return-for-chiropractic-corporations', 'nil-t2-return-for-optometry-corporations', 'nil-t2-return-for-veterinary-corporations',
		'nil-t2-return-for-law-professional-corporations', 'nil-t2-return-for-architecture-corporations', 'nil-t2-return-for-engineering-professional-corporations', 'nil-t2-return-for-land-surveying-corporations',
		'nil-t2-return-for-real-estate-brokerage-corporations', 'nil-t2-return-for-mortgage-brokerage-corporations', 'nil-t2-return-for-insurance-brokerage-corporations', 'nil-t2-return-for-bookkeeping-corporations',
		'nil-t2-return-for-film-production-corporations', 'nil-t2-return-for-music-recording-corporations', 'nil-t2-return-for-esports-corporations', 'nil-t2-return-for-esthetics-corporations',
		'nil-t2-return-for-barbering-corporations', 'nil-t2-return-for-tattoo-studio-corporations', 'nil-t2-return-for-pet-grooming-corporations', 'nil-t2-return-for-auto-repair-corporations',
		'nil-t2-return-for-towing-corporations', 'nil-t2-return-for-car-rental-corporations', 'nil-t2-return-for-equipment-rental-corporations', 'nil-t2-return-for-security-guard-corporations',
		'nil-t2-return-for-janitorial-corporations', 'nil-t2-return-for-snow-removal-corporations', 'nil-t2-return-for-forestry-corporations', 'nil-t2-return-for-mining-exploration-corporations',
		'nil-t2-return-for-oil-and-gas-service-corporations', 'nil-t2-return-for-farming-corporations', 'nil-t2-return-for-greenhouse-corporations', 'nil-t2-return-for-cannabis-corporations',
		'nil-t2-return-for-fishing-corporations', 'nil-t2-return-for-solar-installation-corporations', 'nil-t2-return-for-ev-charging-corporations', 'nil-t2-return-for-drone-services-corporations',
		'nil-t2-return-for-holding-corporations', 'nil-t2-return-for-rental-property-corporations', 'nil-t2-return-for-investment-holding-corporations', 'nil-t2-return-for-dormant-trucking-corporations',
		'nil-t2-return-for-dormant-landscaping-corporations', 'nil-t2-return-for-dormant-restaurant-corporations', 'nil-t2-return-for-dormant-hair-salon-corporations', 'nil-t2-return-for-dormant-gym-corporations',
		'nil-t2-return-for-dormant-daycare-corporations', 'nil-t2-return-for-dormant-ecommerce-corporations', 'nil-t2-return-for-dormant-amazon-fba-corporations', 'nil-t2-return-for-dormant-crypto-trading-corporations',
		'nil-t2-return-for-dormant-photography-corporations', 'nil-t2-return-for-dormant-taxi-corporations', 'nil-t2-return-for-dormant-moving-corporations', 'nil-t2-return-for-dormant-cleaning-corporations',
		'nil-t2-return-for-dormant-hvac-corporations', 'nil-t2-return-for-dormant-plumbing-corporations', 'nil-t2-return-for-dormant-roofing-corporations', 'nil-t2-return-for-dormant-numbered-corporations',
		'nil-t2-return-for-dormant-holding-corporations', 'nil-t2-return-for-dormant-rental-property-corporations', 'nil-t2-return-for-dormant-franchise-corporations', 'nil-t2-return-for-dormant-snow-removal-corporations',
		'nil-t2-return-for-dormant-cannabis-corporations', 'nil-t2-return-for-inactive-it-consulting-corporations', 'nil-t2-return-for-inactive-staffing-agency-corporations', 'nil-t2-return-for-inactive-medical-professional-corporations',
		'nil-t2-return-for-inactive-physiotherapy-corporations', 'nil-t2-return-for-inactive-chiropractic-corporations', 'nil-t2-return-for-inactive-optometry-corporations', 'nil-t2-return-for-inactive-veterinary-corporations',
		'nil-t2-return-for-inactive-law-professional-corporations', 'nil-t2-return-for-inactive-architecture-corporations', 'nil-t2-return-for-inactive-engineering-professional-corporations', 'nil-t2-return-for-inactive-land-surveying-corporations',
		'nil-t2-return-for-inactive-bookkeeping-corporations', 'nil-t2-return-for-inactive-import-corporations', 'nil-t2-return-for-inactive-export-corporations', 'nil-t2-return-for-inactive-wholesale-corporations',
		'nil-t2-return-for-inactive-pharmacy-corporations', 'nil-t2-return-for-struck-off-numbered-corporations', 'nil-t2-return-for-struck-off-federal-corporations', 'nil-t2-return-for-struck-off-ontario-corporations',
		'nil-t2-return-for-struck-off-trucking-corporations', 'nil-t2-return-for-struck-off-restaurant-corporations', 'nil-t2-return-for-pre-revenue-ecommerce-corporations', 'nil-t2-return-for-pre-revenue-mining-exploration-corporations',
		'nil-t2-return-for-pre-revenue-cannabis-corporations', 'nil-t2-return-for-pre-revenue-solar-installation-corporations', 'nil-t2-return-for-pre-revenue-ev-charging-corporations', 'nil-t2-return-for-pre-revenue-esports-corporations',
		'nil-t2-return-for-pre-revenue-drone-services-corporations', 'nil-t2-return-for-pre-revenue-greenhouse-corporations', 'nil-t2-return-for-post-sale-dental-professional-corporations', 'nil-t2-return-for-post-sale-pharmacy-corporations',
		'nil-t2-return-for-post-sale-restaurant-corporations', 'nil-t2-return-for-post-sale-trucking-corporations', 'nil-t2-return-for-post-sale-franchise-corporations', 'nil-t2-return-for-post-sale-real-estate-brokerage-corporations',
		'nil-t2-return-for-post-sale-medical-professional-corporations', 'nil-t2-return-for-wound-down-retail-corporations', 'nil-t2-return-for-wound-down-it-consulting-corporations', 'nil-t2-return-for-wound-down-staffing-agency-corporations',
		'nil-t2-return-for-wound-down-event-planning-corporations', 'nil-t2-return-for-wound-down-travel-agency-corporations', 'nil-t2-return-for-wound-down-film-production-corporations', 'nil-t2-return-for-wound-down-music-recording-corporations',
		'nil-t2-return-for-seasonal-landscaping-corporations', 'nil-t2-return-for-seasonal-snow-removal-corporations', 'nil-t2-return-for-seasonal-farming-corporations', 'nil-t2-return-for-seasonal-greenhouse-corporations',
		'nil-t2-return-for-seasonal-fishing-corporations', 'nil-t2-return-for-seasonal-food-truck-corporations', 'nil-t2-return-for-seasonal-roofing-corporations', 'nil-t2-return-for-seasonal-catering-corporations',
		'nil-t2-return-for-paused-gym-corporations', 'nil-t2-return-for-paused-hair-salon-corporations', 'nil-t2-return-for-paused-daycare-corporations', 'nil-t2-return-for-paused-catering-corporations',
		'nil-t2-return-for-paused-photography-corporations', 'nil-t2-return-for-paused-tattoo-studio-corporations', 'nil-t2-return-for-paused-esthetics-corporations', 'nil-t2-return-for-paused-tutoring-corporations',
		'nil-t2-return-for-shelf-numbered-corporations', 'nil-t2-return-for-shelf-holding-corporations', 'nil-t2-return-for-shelf-federal-corporations', 'nil-t2-return-for-spousal-rental-property-corporations',
		'nil-t2-return-for-spousal-consulting-corporations', 'nil-t2-return-for-spousal-bookkeeping-corporations', 'nil-t2-return-for-spousal-ecommerce-corporations', 'nil-t2-return-for-spousal-holding-corporations',
		'nil-t2-return-for-single-director-consulting-corporations', 'nil-t2-return-for-single-director-trucking-corporations', 'nil-t2-return-for-single-director-it-consulting-corporations', 'nil-t2-return-for-single-director-photography-corporations',
		'nil-t2-return-for-single-director-numbered-corporations', 'nil-t2-return-for-single-director-medical-professional-corporations', 'nil-t2-return-for-two-shareholder-landscaping-corporations', 'nil-t2-return-for-two-shareholder-restaurant-corporations',
		'nil-t2-return-for-two-shareholder-auto-repair-corporations', 'nil-t2-return-for-two-shareholder-holding-corporations', 'nil-t2-return-for-two-shareholder-cleaning-corporations', 'nil-t2-return-for-numbered-holding-corporations',
		'nil-t2-return-for-numbered-rental-property-corporations', 'nil-t2-return-for-numbered-trucking-corporations', 'nil-t2-return-for-numbered-investment-holding-corporations', 'nil-t2-return-for-named-holding-corporations',
		'nil-t2-return-for-named-federal-corporations', 'nil-t2-return-for-named-ontario-corporations', 'nil-t2-return-for-federal-holding-corporations', 'nil-t2-return-for-federal-consulting-corporations',
		'nil-t2-return-for-federal-ecommerce-corporations', 'nil-t2-return-for-federal-numbered-corporations', 'nil-t2-return-for-provincial-holding-corporations', 'nil-t2-return-for-provincial-numbered-corporations',
		'nil-t2-return-for-non-resident-owned-holding-corporations', 'nil-t2-return-for-non-resident-owned-rental-property-corporations', 'nil-t2-return-for-non-resident-owned-ecommerce-corporations', 'nil-t2-return-for-non-resident-owned-consulting-corporations',
		'nil-t2-return-for-non-resident-owned-import-corporations', 'nil-t2-return-for-non-resident-owned-farming-corporations', 'nil-t2-return-for-immigrant-founder-restaurant-corporations', 'nil-t2-return-for-immigrant-founder-trucking-corporations',
		'nil-t2-return-for-immigrant-founder-consulting-corporations', 'nil-t2-return-for-immigrant-founder-grocery-corporations', 'nil-t2-return-for-immigrant-founder-cleaning-corporations', 'nil-t2-return-for-immigrant-founder-ecommerce-corporations',
		'nil-t2-return-for-immigrant-founder-taxi-corporations', 'nil-t2-return-for-student-founder-tutoring-corporations', 'nil-t2-return-for-student-founder-ecommerce-corporations', 'nil-t2-return-for-student-founder-app-development-corporations',
		'nil-t2-return-for-student-founder-esports-corporations', 'nil-t2-return-for-student-founder-photography-corporations', 'nil-t2-return-for-student-founder-drone-services-corporations',
	);
}

/**
 * slug => family code. 215 + 15 + 336 = 566.
 */
function cnf_reserved_slugs() {
	static $map = null;

	if ( null !== $map ) {
		return $map;
	}

	$map = array();

	foreach ( cnf_f1_slugs() as $s ) {
		$map[ $s ] = 'F1';
	}

	foreach ( cnf_cities() as $city ) {
		$map[ 'nil-corporate-tax-filing-' . $city ] = 'F3';
	}

	$places = array_merge( cnf_cities(), cnf_jurisdictions() );

	foreach ( cnf_service_patterns() as $pattern ) {
		foreach ( $places as $place ) {
			$map[ sprintf( $pattern, $place ) ] = 'F4';
		}
	}

	return $map;
}

function cnf_is_reserved_slug( $slug ) {
	$map  = cnf_reserved_slugs();
	$slug = sanitize_title( $slug );
	return isset( $map[ $slug ] ) ? $map[ $slug ] : false;
}

/** Paths WordPress or a plugin owns. Never resolved as a root item. */
function cnf_system_slugs() {
	return array(
		'wp-json', 'wp-admin', 'wp-login.php', 'wp-cron.php', 'xmlrpc.php',
		'robots.txt', 'favicon.ico', 'sitemap.xml', 'sitemap_index.xml',
		'wp-sitemap.xml', 'feed', 'rss', 'rss2', 'atom', 'embed', 'comments',
	);
}

/* 1. Root permalinks -------------------------------------------------- */

add_filter( 'post_type_link', 'cnf_root_permalink', 10, 2 );
function cnf_root_permalink( $link, $post ) {
	if ( in_array( $post->post_type, cnf_root_types(), true ) && $post->post_name ) {
		return home_url( '/' . $post->post_name . '/' );
	}
	return $link;
}

/* 2. One catch-all rule, directly before the page rule ----------------- */

add_filter( 'rewrite_rules_array', 'cnf_inject_root_rule' );
function cnf_inject_root_rule( $rules ) {
	$ours  = array( '^([^/]+)/?$' => 'index.php?cnf_root=$matches[1]' );
	$built = array();
	$done  = false;

	foreach ( $rules as $regex => $query ) {
		if ( ! $done && false !== strpos( $query, 'pagename=' ) ) {
			$built = array_merge( $built, $ours );
			$done  = true;
		}
		$built[ $regex ] = $query;
	}

	if ( ! $done ) {
		$built = array_merge( $built, $ours );
	}

	return $built;
}

add_filter( 'query_vars', 'cnf_register_query_var' );
function cnf_register_query_var( $vars ) {
	$vars[] = 'cnf_root';
	return $vars;
}

/* 3. Resolve the slug -------------------------------------------------- */

add_filter( 'request', 'cnf_resolve_root_request' );
function cnf_resolve_root_request( $vars ) {
	if ( empty( $vars['cnf_root'] ) ) {
		return $vars;
	}

	$slug = sanitize_title( wp_unslash( $vars['cnf_root'] ) );
	unset( $vars['cnf_root'] );

	if ( '' === $slug || in_array( $slug, cnf_system_slugs(), true ) ) {
		return $vars;
	}

	$post_type = cnf_lookup_root_slug( $slug );

	if ( $post_type ) {
		$vars['post_type'] = $post_type;
		$vars['name']      = $slug;
		return $vars;
	}

	$vars['pagename'] = $slug;
	return $vars;
}

function cnf_lookup_root_slug( $slug ) {
	global $wpdb;

	$types    = cnf_root_types();
	$statuses = array( 'publish' );

	if ( is_user_logged_in() && current_user_can( 'edit_posts' ) ) {
		$statuses = array_merge( $statuses, array( 'draft', 'pending', 'private', 'future' ) );
	}

	$type_ph   = implode( ',', array_fill( 0, count( $types ), '%s' ) );
	$status_ph = implode( ',', array_fill( 0, count( $statuses ), '%s' ) );

	$sql = $wpdb->prepare(
		"SELECT post_type FROM {$wpdb->posts}
		  WHERE post_name = %s
		    AND post_type IN ( {$type_ph} )
		    AND post_status IN ( {$status_ph} )
		  LIMIT 1",
		array_merge( array( $slug ), $types, $statuses )
	);

	return $wpdb->get_var( $sql );
}

/* 4. Reserved slug guard ----------------------------------------------- */

add_filter( 'wp_unique_post_slug', 'cnf_guard_reserved_slug', 10, 6 );
function cnf_guard_reserved_slug( $slug, $post_ID, $post_status, $post_type, $post_parent, $original_slug ) {
	if ( in_array( $post_type, cnf_root_types(), true ) ) {
		return $slug;
	}

	$family = cnf_is_reserved_slug( $slug );

	if ( $family ) {
		error_log( sprintf(
			'[cnf] blocked %s #%d from taking reserved %s slug "%s"',
			$post_type, (int) $post_ID, $family, $slug
		) );
		return $slug . '-reserved';
	}

	return $slug;
}

foreach ( array( 'post', 'page' ) as $cnf_guarded_type ) {
	add_filter( "rest_pre_insert_{$cnf_guarded_type}", 'cnf_rest_refuse_reserved', 10, 2 );
}
function cnf_rest_refuse_reserved( $prepared, $request ) {
	$slug = $request->get_param( 'slug' );

	if ( ! $slug ) {
		return $prepared;
	}

	$family = cnf_is_reserved_slug( $slug );

	if ( $family ) {
		return new WP_Error(
			'cnf_reserved_slug',
			sprintf( 'The slug "%s" is reserved for Family %s and cannot be used.', sanitize_title( $slug ), substr( $family, 1 ) ),
			array( 'status' => 409 )
		);
	}

	return $prepared;
}

/** Pre-flight for the Python pipeline: check before creating, not after. */
add_action( 'rest_api_init', 'cnf_register_slug_check' );
function cnf_register_slug_check() {
	register_rest_route( 'cnf/v1', '/slug-check', array(
		'methods'             => 'GET',
		'permission_callback' => function () { return current_user_can( 'edit_posts' ); },
		'args'                => array( 'slug' => array( 'required' => true, 'type' => 'string' ) ),
		'callback'            => function ( $request ) {
			$slug   = sanitize_title( $request->get_param( 'slug' ) );
			$family = cnf_is_reserved_slug( $slug );

			return array(
				'slug'     => $slug,
				'reserved' => (bool) $family,
				'family'   => $family ? $family : null,
				'taken_by' => cnf_lookup_root_slug( $slug ) ?: null,
				'total'    => count( cnf_reserved_slugs() ),
			);
		},
	) );
}

/* 5. Flush once per version -------------------------------------------- */

add_action( 'init', 'cnf_maybe_flush_rules', 999 );
function cnf_maybe_flush_rules() {
	if ( get_option( 'cnf_router_version' ) === CNF_ROUTER_VERSION ) {
		return;
	}

	flush_rewrite_rules( false );
	update_option( 'cnf_router_version', CNF_ROUTER_VERSION, false );
}
