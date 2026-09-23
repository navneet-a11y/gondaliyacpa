<?php
/**
 * cnf-root-router — corpnilfilingfor300.ca
 *
 * WPCode Lite snippet. Type: PHP Snippet. Location: Run Everywhere. Priority: 10.
 *
 * Three post types live at the site root with no URL prefix:
 *   nil_vertical (215)  nil_city_hub (15)  nil_service_place (336)
 *
 * WordPress cannot give three post types an empty rewrite slug. Each would
 * register its own catch-all rule, the first registered would win every
 * single-segment request, and a slug belonging to either of the other two
 * would 404. So all three are registered in CPT UI with rewrite = false and
 * this snippet owns their URLs instead:
 *
 *   1. post_type_link  gives each item its root permalink
 *   2. ONE catch-all rule, injected immediately before WordPress's page rule
 *      so every core rule (REST, feeds, sitemaps, the ten folder post types)
 *      still matches first, and pages keep working
 *   3. the request filter resolves the slug in a single indexed query
 *   4. the 566 reserved slugs cannot be taken by a page, post or hub
 *   5. rewrite rules flush once per version, never on every page load
 */

if ( ! defined( 'ABSPATH' ) ) { exit; }

define( 'CNF_ROUTER_VERSION', '1.0.0' );

function cnf_root_types() {
	return array( 'nil_vertical', 'nil_city_hub', 'nil_service_place' );
}

/**
 * Paths WordPress or a plugin owns. Never resolved as a root item.
 */
function cnf_system_slugs() {
	return array(
		'wp-json', 'wp-admin', 'wp-login.php', 'wp-cron.php', 'xmlrpc.php',
		'robots.txt', 'favicon.ico', 'sitemap.xml', 'sitemap_index.xml',
		'wp-sitemap.xml', 'feed', 'rss', 'rss2', 'atom', 'embed', 'comments',
	);
}

/* ------------------------------------------------------------------ *
 * 1. Root permalinks
 * ------------------------------------------------------------------ */

add_filter( 'post_type_link', 'cnf_root_permalink', 10, 2 );
function cnf_root_permalink( $link, $post ) {
	if ( in_array( $post->post_type, cnf_root_types(), true ) && $post->post_name ) {
		return home_url( '/' . $post->post_name . '/' );
	}
	return $link;
}

/* ------------------------------------------------------------------ *
 * 2. One catch-all rule, placed directly before the page rule
 * ------------------------------------------------------------------ */

add_filter( 'rewrite_rules_array', 'cnf_inject_root_rule' );
function cnf_inject_root_rule( $rules ) {
	$ours  = array( '^([^/]+)/?$' => 'index.php?cnf_root=$matches[1]' );
	$built = array();
	$done  = false;

	foreach ( $rules as $regex => $query ) {
		// The page rule is the last thing that can swallow a single segment.
		// Insert ahead of it so folder post types and core rules win first.
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

/* ------------------------------------------------------------------ *
 * 3. Resolve the slug
 * ------------------------------------------------------------------ */

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

	// Not one of ours. Hand it back to the page rule's behaviour so real
	// pages resolve and anything genuinely missing 404s as normal.
	$vars['pagename'] = $slug;
	return $vars;
}

/**
 * One indexed lookup against the three root types.
 * Editors also see draft, pending and private so test items are checkable.
 */
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

/* ------------------------------------------------------------------ *
 * 4. Reserved slugs — 566 across F1, F3 and F4
 * ------------------------------------------------------------------ */

function cnf_reserved_slugs() {
	static $map = null;

	if ( null !== $map ) {
		return $map;
	}

	$f1 = array(
	'nil-t2-return-for-dormant-consulting-corporations', 'nil-t2-return-for-real-estate-numbered-corporations', 'nil-t2-return-for-trucking-corporations',
	'nil-t2-return-for-dental-professional-corporations', 'nil-t2-return-for-shell-corporations', 'nil-t2-return-for-landscaping-corporations',
	'nil-t2-return-for-medical-professional-corporations', 'nil-t2-return-for-it-consulting-corporations', 'nil-t2-return-for-staffing-agency-corporations',
	'nil-t2-return-for-restaurant-corporations', 'nil-t2-return-for-hair-salon-corporations', 'nil-t2-return-for-gym-corporations',
	'nil-t2-return-for-daycare-corporations', 'nil-t2-return-for-ecommerce-corporations', 'nil-t2-return-for-amazon-fba-corporations',
	'nil-t2-return-for-crypto-trading-corporations', 'nil-t2-return-for-photography-corporations', 'nil-t2-return-for-taxi-corporations',
	'nil-t2-return-for-moving-corporations', 'nil-t2-return-for-cleaning-corporations', 'nil-t2-return-for-hvac-corporations',
	'nil-t2-return-for-plumbing-corporations', 'nil-t2-return-for-electrical-contracting-corporations', 'nil-t2-return-for-roofing-corporations',
	'nil-t2-return-for-flooring-corporations', 'nil-t2-return-for-painting-corporations', 'nil-t2-return-for-drywall-corporations',
	'nil-t2-return-for-welding-corporations', 'nil-t2-return-for-machine-shop-corporations', 'nil-t2-return-for-printing-corporations',
	'nil-t2-return-for-signage-corporations', 'nil-t2-return-for-tutoring-corporations', 'nil-t2-return-for-translation-corporations',
	'nil-t2-return-for-travel-agency-corporations', 'nil-t2-return-for-event-planning-corporations', 'nil-t2-return-for-catering-corporations',
	'nil-t2-return-for-food-truck-corporations', 'nil-t2-return-for-bakery-corporations', 'nil-t2-return-for-brewery-corporations',
	'nil-t2-return-for-franchise-corporations', 'nil-t2-return-for-import-corporations', 'nil-t2-return-for-export-corporations',
	'nil-t2-return-for-wholesale-corporations', 'nil-t2-return-for-pharmacy-corporations', 'nil-t2-return-for-physiotherapy-corporations',
	'nil-t2-return-for-chiropractic-corporations', 'nil-t2-return-for-optometry-corporations', 'nil-t2-return-for-veterinary-corporations',
	'nil-t2-return-for-law-professional-corporations', 'nil-t2-return-for-architecture-corporations', 'nil-t2-return-for-engineering-professional-corporations',
	'nil-t2-return-for-land-surveying-corporations', 'nil-t2-return-for-real-estate-brokerage-corporations', 'nil-t2-return-for-mortgage-brokerage-corporations',
	'nil-t2-return-for-insurance-brokerage-corporations', 'nil-t2-return-for-bookkeeping-corporations', 'nil-t2-return-for-film-production-corporations',
	'nil-t2-return-for-music-recording-corporations', 'nil-t2-return-for-esports-corporations', 'nil-t2-return-for-esthetics-corporations',
	'nil-t2-return-for-barbering-corporations', 'nil-t2-return-for-tattoo-studio-corporations', 'nil-t2-return-for-pet-grooming-corporations',
	'nil-t2-return-for-auto-repair-corporations', 'nil-t2-return-for-towing-corporations', 'nil-t2-return-for-car-rental-corporations',
	'nil-t2-return-for-equipment-rental-corporations', 'nil-t2-return-for-security-guard-corporations', 'nil-t2-return-for-janitorial-corporations',
	'nil-t2-return-for-snow-removal-corporations', 'nil-t2-return-for-forestry-corporations', 'nil-t2-return-for-mining-exploration-corporations',
	'nil-t2-return-for-oil-and-gas-service-corporations', 'nil-t2-return-for-farming-corporations', 'nil-t2-return-for-greenhouse-corporations',
	'nil-t2-return-for-cannabis-corporations', 'nil-t2-return-for-fishing-corporations', 'nil-t2-return-for-solar-installation-corporations',
	'nil-t2-return-for-ev-charging-corporations', 'nil-t2-return-for-drone-services-corporations', 'nil-t2-return-for-holding-corporations',
	'nil-t2-return-for-rental-property-corporations', 'nil-t2-return-for-investment-holding-corporations', 'nil-t2-return-for-dormant-trucking-corporations',
	'nil-t2-return-for-dormant-landscaping-corporations', 'nil-t2-return-for-dormant-restaurant-corporations', 'nil-t2-return-for-dormant-hair-salon-corporations',
	'nil-t2-return-for-dormant-gym-corporations', 'nil-t2-return-for-dormant-daycare-corporations', 'nil-t2-return-for-dormant-ecommerce-corporations',
	'nil-t2-return-for-dormant-amazon-fba-corporations', 'nil-t2-return-for-dormant-crypto-trading-corporations', 'nil-t2-return-for-dormant-photography-corporations',
	'nil-t2-return-for-dormant-taxi-corporations', 'nil-t2-return-for-dormant-moving-corporations', 'nil-t2-return-for-dormant-cleaning-corporations',
	'nil-t2-return-for-dormant-hvac-corporations', 'nil-t2-return-for-dormant-plumbing-corporations', 'nil-t2-return-for-dormant-roofing-corporations',
	'nil-t2-return-for-dormant-numbered-corporations', 'nil-t2-return-for-dormant-holding-corporations', 'nil-t2-return-for-dormant-rental-property-corporations',
	'nil-t2-return-for-dormant-franchise-corporations', 'nil-t2-return-for-dormant-snow-removal-corporations', 'nil-t2-return-for-dormant-cannabis-corporations',
	'nil-t2-return-for-inactive-it-consulting-corporations', 'nil-t2-return-for-inactive-staffing-agency-corporations', 'nil-t2-return-for-inactive-medical-professional-corporations',
	'nil-t2-return-for-inactive-physiotherapy-corporations', 'nil-t2-return-for-inactive-chiropractic-corporations', 'nil-t2-return-for-inactive-optometry-corporations',
	'nil-t2-return-for-inactive-veterinary-corporations', 'nil-t2-return-for-inactive-law-professional-corporations', 'nil-t2-return-for-inactive-architecture-corporations',
	'nil-t2-return-for-inactive-engineering-professional-corporations', 'nil-t2-return-for-inactive-land-surveying-corporations', 'nil-t2-return-for-inactive-bookkeeping-corporations',
	'nil-t2-return-for-inactive-import-corporations', 'nil-t2-return-for-inactive-export-corporations', 'nil-t2-return-for-inactive-wholesale-corporations',
	'nil-t2-return-for-inactive-pharmacy-corporations', 'nil-t2-return-for-struck-off-numbered-corporations', 'nil-t2-return-for-struck-off-federal-corporations',
	'nil-t2-return-for-struck-off-ontario-corporations', 'nil-t2-return-for-struck-off-trucking-corporations', 'nil-t2-return-for-struck-off-restaurant-corporations',
	'nil-t2-return-for-pre-revenue-ecommerce-corporations', 'nil-t2-return-for-pre-revenue-mining-exploration-corporations', 'nil-t2-return-for-pre-revenue-cannabis-corporations',
	'nil-t2-return-for-pre-revenue-solar-installation-corporations', 'nil-t2-return-for-pre-revenue-ev-charging-corporations', 'nil-t2-return-for-pre-revenue-esports-corporations',
	'nil-t2-return-for-pre-revenue-drone-services-corporations', 'nil-t2-return-for-pre-revenue-greenhouse-corporations', 'nil-t2-return-for-post-sale-dental-professional-corporations',
	'nil-t2-return-for-post-sale-pharmacy-corporations', 'nil-t2-return-for-post-sale-restaurant-corporations', 'nil-t2-return-for-post-sale-trucking-corporations',
	'nil-t2-return-for-post-sale-franchise-corporations', 'nil-t2-return-for-post-sale-real-estate-brokerage-corporations', 'nil-t2-return-for-post-sale-medical-professional-corporations',
	'nil-t2-return-for-wound-down-retail-corporations', 'nil-t2-return-for-wound-down-it-consulting-corporations', 'nil-t2-return-for-wound-down-staffing-agency-corporations',
	'nil-t2-return-for-wound-down-event-planning-corporations', 'nil-t2-return-for-wound-down-travel-agency-corporations', 'nil-t2-return-for-wound-down-film-production-corporations',
	'nil-t2-return-for-wound-down-music-recording-corporations', 'nil-t2-return-for-seasonal-landscaping-corporations', 'nil-t2-return-for-seasonal-snow-removal-corporations',
	'nil-t2-return-for-seasonal-farming-corporations', 'nil-t2-return-for-seasonal-greenhouse-corporations', 'nil-t2-return-for-seasonal-fishing-corporations',
	'nil-t2-return-for-seasonal-food-truck-corporations', 'nil-t2-return-for-seasonal-roofing-corporations', 'nil-t2-return-for-seasonal-catering-corporations',
	'nil-t2-return-for-paused-gym-corporations', 'nil-t2-return-for-paused-hair-salon-corporations', 'nil-t2-return-for-paused-daycare-corporations',
	'nil-t2-return-for-paused-catering-corporations', 'nil-t2-return-for-paused-photography-corporations', 'nil-t2-return-for-paused-tattoo-studio-corporations',
	'nil-t2-return-for-paused-esthetics-corporations', 'nil-t2-return-for-paused-tutoring-corporations', 'nil-t2-return-for-shelf-numbered-corporations',
	'nil-t2-return-for-shelf-holding-corporations', 'nil-t2-return-for-shelf-federal-corporations', 'nil-t2-return-for-spousal-rental-property-corporations',
	'nil-t2-return-for-spousal-consulting-corporations', 'nil-t2-return-for-spousal-bookkeeping-corporations', 'nil-t2-return-for-spousal-ecommerce-corporations',
	'nil-t2-return-for-spousal-holding-corporations', 'nil-t2-return-for-single-director-consulting-corporations', 'nil-t2-return-for-single-director-trucking-corporations',
	'nil-t2-return-for-single-director-it-consulting-corporations', 'nil-t2-return-for-single-director-photography-corporations', 'nil-t2-return-for-single-director-numbered-corporations',
	'nil-t2-return-for-single-director-medical-professional-corporations', 'nil-t2-return-for-two-shareholder-landscaping-corporations', 'nil-t2-return-for-two-shareholder-restaurant-corporations',
	'nil-t2-return-for-two-shareholder-auto-repair-corporations', 'nil-t2-return-for-two-shareholder-holding-corporations', 'nil-t2-return-for-two-shareholder-cleaning-corporations',
	'nil-t2-return-for-numbered-holding-corporations', 'nil-t2-return-for-numbered-rental-property-corporations', 'nil-t2-return-for-numbered-trucking-corporations',
	'nil-t2-return-for-numbered-investment-holding-corporations', 'nil-t2-return-for-named-holding-corporations', 'nil-t2-return-for-named-federal-corporations',
	'nil-t2-return-for-named-ontario-corporations', 'nil-t2-return-for-federal-holding-corporations', 'nil-t2-return-for-federal-consulting-corporations',
	'nil-t2-return-for-federal-ecommerce-corporations', 'nil-t2-return-for-federal-numbered-corporations', 'nil-t2-return-for-provincial-holding-corporations',
	'nil-t2-return-for-provincial-numbered-corporations', 'nil-t2-return-for-non-resident-owned-holding-corporations', 'nil-t2-return-for-non-resident-owned-rental-property-corporations',
	'nil-t2-return-for-non-resident-owned-ecommerce-corporations', 'nil-t2-return-for-non-resident-owned-consulting-corporations', 'nil-t2-return-for-non-resident-owned-import-corporations',
	'nil-t2-return-for-non-resident-owned-farming-corporations', 'nil-t2-return-for-immigrant-founder-restaurant-corporations', 'nil-t2-return-for-immigrant-founder-trucking-corporations',
	'nil-t2-return-for-immigrant-founder-consulting-corporations', 'nil-t2-return-for-immigrant-founder-grocery-corporations', 'nil-t2-return-for-immigrant-founder-cleaning-corporations',
	'nil-t2-return-for-immigrant-founder-ecommerce-corporations', 'nil-t2-return-for-immigrant-founder-taxi-corporations', 'nil-t2-return-for-student-founder-tutoring-corporations',
	'nil-t2-return-for-student-founder-ecommerce-corporations', 'nil-t2-return-for-student-founder-app-development-corporations', 'nil-t2-return-for-student-founder-esports-corporations',
	'nil-t2-return-for-student-founder-photography-corporations', 'nil-t2-return-for-student-founder-drone-services-corporations',
	);

	$f3 = array(
	'nil-corporate-tax-filing-toronto', 'nil-corporate-tax-filing-mississauga', 'nil-corporate-tax-filing-brampton',
	'nil-corporate-tax-filing-scarborough', 'nil-corporate-tax-filing-etobicoke', 'nil-corporate-tax-filing-north-york',
	'nil-corporate-tax-filing-markham', 'nil-corporate-tax-filing-vaughan', 'nil-corporate-tax-filing-richmond-hill',
	'nil-corporate-tax-filing-oakville', 'nil-corporate-tax-filing-ottawa', 'nil-corporate-tax-filing-oshawa',
	'nil-corporate-tax-filing-guelph', 'nil-corporate-tax-filing-hamilton', 'nil-corporate-tax-filing-windsor',
	);

	$f4 = array(
	'nil-t2-filing-toronto', 'nil-t2-filing-mississauga', 'nil-t2-filing-brampton',
	'nil-t2-filing-scarborough', 'nil-t2-filing-etobicoke', 'nil-t2-filing-north-york',
	'nil-t2-filing-markham', 'nil-t2-filing-vaughan', 'nil-t2-filing-richmond-hill',
	'nil-t2-filing-oakville', 'nil-t2-filing-ottawa', 'nil-t2-filing-oshawa',
	'nil-t2-filing-guelph', 'nil-t2-filing-hamilton', 'nil-t2-filing-windsor',
	'nil-t2-filing-ontario', 'nil-t2-filing-quebec', 'nil-t2-filing-british-columbia',
	'nil-t2-filing-alberta', 'nil-t2-filing-manitoba', 'nil-t2-filing-saskatchewan',
	'nil-t2-filing-nova-scotia', 'nil-t2-filing-new-brunswick', 'nil-t2-filing-newfoundland-and-labrador',
	'nil-t2-filing-prince-edward-island', 'nil-t2-filing-yukon', 'nil-t2-filing-northwest-territories',
	'nil-t2-filing-nunavut', 'catch-up-nil-t2-filing-toronto', 'catch-up-nil-t2-filing-mississauga',
	'catch-up-nil-t2-filing-brampton', 'catch-up-nil-t2-filing-scarborough', 'catch-up-nil-t2-filing-etobicoke',
	'catch-up-nil-t2-filing-north-york', 'catch-up-nil-t2-filing-markham', 'catch-up-nil-t2-filing-vaughan',
	'catch-up-nil-t2-filing-richmond-hill', 'catch-up-nil-t2-filing-oakville', 'catch-up-nil-t2-filing-ottawa',
	'catch-up-nil-t2-filing-oshawa', 'catch-up-nil-t2-filing-guelph', 'catch-up-nil-t2-filing-hamilton',
	'catch-up-nil-t2-filing-windsor', 'catch-up-nil-t2-filing-ontario', 'catch-up-nil-t2-filing-quebec',
	'catch-up-nil-t2-filing-british-columbia', 'catch-up-nil-t2-filing-alberta', 'catch-up-nil-t2-filing-manitoba',
	'catch-up-nil-t2-filing-saskatchewan', 'catch-up-nil-t2-filing-nova-scotia', 'catch-up-nil-t2-filing-new-brunswick',
	'catch-up-nil-t2-filing-newfoundland-and-labrador', 'catch-up-nil-t2-filing-prince-edward-island', 'catch-up-nil-t2-filing-yukon',
	'catch-up-nil-t2-filing-northwest-territories', 'catch-up-nil-t2-filing-nunavut', 'dormant-corporation-filing-toronto',
	'dormant-corporation-filing-mississauga', 'dormant-corporation-filing-brampton', 'dormant-corporation-filing-scarborough',
	'dormant-corporation-filing-etobicoke', 'dormant-corporation-filing-north-york', 'dormant-corporation-filing-markham',
	'dormant-corporation-filing-vaughan', 'dormant-corporation-filing-richmond-hill', 'dormant-corporation-filing-oakville',
	'dormant-corporation-filing-ottawa', 'dormant-corporation-filing-oshawa', 'dormant-corporation-filing-guelph',
	'dormant-corporation-filing-hamilton', 'dormant-corporation-filing-windsor', 'dormant-corporation-filing-ontario',
	'dormant-corporation-filing-quebec', 'dormant-corporation-filing-british-columbia', 'dormant-corporation-filing-alberta',
	'dormant-corporation-filing-manitoba', 'dormant-corporation-filing-saskatchewan', 'dormant-corporation-filing-nova-scotia',
	'dormant-corporation-filing-new-brunswick', 'dormant-corporation-filing-newfoundland-and-labrador', 'dormant-corporation-filing-prince-edward-island',
	'dormant-corporation-filing-yukon', 'dormant-corporation-filing-northwest-territories', 'dormant-corporation-filing-nunavut',
	'final-t2-before-dissolution-toronto', 'final-t2-before-dissolution-mississauga', 'final-t2-before-dissolution-brampton',
	'final-t2-before-dissolution-scarborough', 'final-t2-before-dissolution-etobicoke', 'final-t2-before-dissolution-north-york',
	'final-t2-before-dissolution-markham', 'final-t2-before-dissolution-vaughan', 'final-t2-before-dissolution-richmond-hill',
	'final-t2-before-dissolution-oakville', 'final-t2-before-dissolution-ottawa', 'final-t2-before-dissolution-oshawa',
	'final-t2-before-dissolution-guelph', 'final-t2-before-dissolution-hamilton', 'final-t2-before-dissolution-windsor',
	'final-t2-before-dissolution-ontario', 'final-t2-before-dissolution-quebec', 'final-t2-before-dissolution-british-columbia',
	'final-t2-before-dissolution-alberta', 'final-t2-before-dissolution-manitoba', 'final-t2-before-dissolution-saskatchewan',
	'final-t2-before-dissolution-nova-scotia', 'final-t2-before-dissolution-new-brunswick', 'final-t2-before-dissolution-newfoundland-and-labrador',
	'final-t2-before-dissolution-prince-edward-island', 'final-t2-before-dissolution-yukon', 'final-t2-before-dissolution-northwest-territories',
	'final-t2-before-dissolution-nunavut', 't2-short-filing-toronto', 't2-short-filing-mississauga',
	't2-short-filing-brampton', 't2-short-filing-scarborough', 't2-short-filing-etobicoke',
	't2-short-filing-north-york', 't2-short-filing-markham', 't2-short-filing-vaughan',
	't2-short-filing-richmond-hill', 't2-short-filing-oakville', 't2-short-filing-ottawa',
	't2-short-filing-oshawa', 't2-short-filing-guelph', 't2-short-filing-hamilton',
	't2-short-filing-windsor', 't2-short-filing-ontario', 't2-short-filing-quebec',
	't2-short-filing-british-columbia', 't2-short-filing-alberta', 't2-short-filing-manitoba',
	't2-short-filing-saskatchewan', 't2-short-filing-nova-scotia', 't2-short-filing-new-brunswick',
	't2-short-filing-newfoundland-and-labrador', 't2-short-filing-prince-edward-island', 't2-short-filing-yukon',
	't2-short-filing-northwest-territories', 't2-short-filing-nunavut', 'nil-t2-filing-cost-in-toronto',
	'nil-t2-filing-cost-in-mississauga', 'nil-t2-filing-cost-in-brampton', 'nil-t2-filing-cost-in-scarborough',
	'nil-t2-filing-cost-in-etobicoke', 'nil-t2-filing-cost-in-north-york', 'nil-t2-filing-cost-in-markham',
	'nil-t2-filing-cost-in-vaughan', 'nil-t2-filing-cost-in-richmond-hill', 'nil-t2-filing-cost-in-oakville',
	'nil-t2-filing-cost-in-ottawa', 'nil-t2-filing-cost-in-oshawa', 'nil-t2-filing-cost-in-guelph',
	'nil-t2-filing-cost-in-hamilton', 'nil-t2-filing-cost-in-windsor', 'nil-t2-filing-cost-in-ontario',
	'nil-t2-filing-cost-in-quebec', 'nil-t2-filing-cost-in-british-columbia', 'nil-t2-filing-cost-in-alberta',
	'nil-t2-filing-cost-in-manitoba', 'nil-t2-filing-cost-in-saskatchewan', 'nil-t2-filing-cost-in-nova-scotia',
	'nil-t2-filing-cost-in-new-brunswick', 'nil-t2-filing-cost-in-newfoundland-and-labrador', 'nil-t2-filing-cost-in-prince-edward-island',
	'nil-t2-filing-cost-in-yukon', 'nil-t2-filing-cost-in-northwest-territories', 'nil-t2-filing-cost-in-nunavut',
	'unfiled-corporate-tax-returns-toronto', 'unfiled-corporate-tax-returns-mississauga', 'unfiled-corporate-tax-returns-brampton',
	'unfiled-corporate-tax-returns-scarborough', 'unfiled-corporate-tax-returns-etobicoke', 'unfiled-corporate-tax-returns-north-york',
	'unfiled-corporate-tax-returns-markham', 'unfiled-corporate-tax-returns-vaughan', 'unfiled-corporate-tax-returns-richmond-hill',
	'unfiled-corporate-tax-returns-oakville', 'unfiled-corporate-tax-returns-ottawa', 'unfiled-corporate-tax-returns-oshawa',
	'unfiled-corporate-tax-returns-guelph', 'unfiled-corporate-tax-returns-hamilton', 'unfiled-corporate-tax-returns-windsor',
	'unfiled-corporate-tax-returns-ontario', 'unfiled-corporate-tax-returns-quebec', 'unfiled-corporate-tax-returns-british-columbia',
	'unfiled-corporate-tax-returns-alberta', 'unfiled-corporate-tax-returns-manitoba', 'unfiled-corporate-tax-returns-saskatchewan',
	'unfiled-corporate-tax-returns-nova-scotia', 'unfiled-corporate-tax-returns-new-brunswick', 'unfiled-corporate-tax-returns-newfoundland-and-labrador',
	'unfiled-corporate-tax-returns-prince-edward-island', 'unfiled-corporate-tax-returns-yukon', 'unfiled-corporate-tax-returns-northwest-territories',
	'unfiled-corporate-tax-returns-nunavut', 'no-activity-corporation-tax-return-toronto', 'no-activity-corporation-tax-return-mississauga',
	'no-activity-corporation-tax-return-brampton', 'no-activity-corporation-tax-return-scarborough', 'no-activity-corporation-tax-return-etobicoke',
	'no-activity-corporation-tax-return-north-york', 'no-activity-corporation-tax-return-markham', 'no-activity-corporation-tax-return-vaughan',
	'no-activity-corporation-tax-return-richmond-hill', 'no-activity-corporation-tax-return-oakville', 'no-activity-corporation-tax-return-ottawa',
	'no-activity-corporation-tax-return-oshawa', 'no-activity-corporation-tax-return-guelph', 'no-activity-corporation-tax-return-hamilton',
	'no-activity-corporation-tax-return-windsor', 'no-activity-corporation-tax-return-ontario', 'no-activity-corporation-tax-return-quebec',
	'no-activity-corporation-tax-return-british-columbia', 'no-activity-corporation-tax-return-alberta', 'no-activity-corporation-tax-return-manitoba',
	'no-activity-corporation-tax-return-saskatchewan', 'no-activity-corporation-tax-return-nova-scotia', 'no-activity-corporation-tax-return-new-brunswick',
	'no-activity-corporation-tax-return-newfoundland-and-labrador', 'no-activity-corporation-tax-return-prince-edward-island', 'no-activity-corporation-tax-return-yukon',
	'no-activity-corporation-tax-return-northwest-territories', 'no-activity-corporation-tax-return-nunavut', 'numbered-corporation-nil-filing-toronto',
	'numbered-corporation-nil-filing-mississauga', 'numbered-corporation-nil-filing-brampton', 'numbered-corporation-nil-filing-scarborough',
	'numbered-corporation-nil-filing-etobicoke', 'numbered-corporation-nil-filing-north-york', 'numbered-corporation-nil-filing-markham',
	'numbered-corporation-nil-filing-vaughan', 'numbered-corporation-nil-filing-richmond-hill', 'numbered-corporation-nil-filing-oakville',
	'numbered-corporation-nil-filing-ottawa', 'numbered-corporation-nil-filing-oshawa', 'numbered-corporation-nil-filing-guelph',
	'numbered-corporation-nil-filing-hamilton', 'numbered-corporation-nil-filing-windsor', 'numbered-corporation-nil-filing-ontario',
	'numbered-corporation-nil-filing-quebec', 'numbered-corporation-nil-filing-british-columbia', 'numbered-corporation-nil-filing-alberta',
	'numbered-corporation-nil-filing-manitoba', 'numbered-corporation-nil-filing-saskatchewan', 'numbered-corporation-nil-filing-nova-scotia',
	'numbered-corporation-nil-filing-new-brunswick', 'numbered-corporation-nil-filing-newfoundland-and-labrador', 'numbered-corporation-nil-filing-prince-edward-island',
	'numbered-corporation-nil-filing-yukon', 'numbered-corporation-nil-filing-northwest-territories', 'numbered-corporation-nil-filing-nunavut',
	'inactive-holding-corporation-t2-filing-toronto', 'inactive-holding-corporation-t2-filing-mississauga', 'inactive-holding-corporation-t2-filing-brampton',
	'inactive-holding-corporation-t2-filing-scarborough', 'inactive-holding-corporation-t2-filing-etobicoke', 'inactive-holding-corporation-t2-filing-north-york',
	'inactive-holding-corporation-t2-filing-markham', 'inactive-holding-corporation-t2-filing-vaughan', 'inactive-holding-corporation-t2-filing-richmond-hill',
	'inactive-holding-corporation-t2-filing-oakville', 'inactive-holding-corporation-t2-filing-ottawa', 'inactive-holding-corporation-t2-filing-oshawa',
	'inactive-holding-corporation-t2-filing-guelph', 'inactive-holding-corporation-t2-filing-hamilton', 'inactive-holding-corporation-t2-filing-windsor',
	'inactive-holding-corporation-t2-filing-ontario', 'inactive-holding-corporation-t2-filing-quebec', 'inactive-holding-corporation-t2-filing-british-columbia',
	'inactive-holding-corporation-t2-filing-alberta', 'inactive-holding-corporation-t2-filing-manitoba', 'inactive-holding-corporation-t2-filing-saskatchewan',
	'inactive-holding-corporation-t2-filing-nova-scotia', 'inactive-holding-corporation-t2-filing-new-brunswick', 'inactive-holding-corporation-t2-filing-newfoundland-and-labrador',
	'inactive-holding-corporation-t2-filing-prince-edward-island', 'inactive-holding-corporation-t2-filing-yukon', 'inactive-holding-corporation-t2-filing-northwest-territories',
	'inactive-holding-corporation-t2-filing-nunavut', 'nil-t2-filing-deadline-toronto', 'nil-t2-filing-deadline-mississauga',
	'nil-t2-filing-deadline-brampton', 'nil-t2-filing-deadline-scarborough', 'nil-t2-filing-deadline-etobicoke',
	'nil-t2-filing-deadline-north-york', 'nil-t2-filing-deadline-markham', 'nil-t2-filing-deadline-vaughan',
	'nil-t2-filing-deadline-richmond-hill', 'nil-t2-filing-deadline-oakville', 'nil-t2-filing-deadline-ottawa',
	'nil-t2-filing-deadline-oshawa', 'nil-t2-filing-deadline-guelph', 'nil-t2-filing-deadline-hamilton',
	'nil-t2-filing-deadline-windsor', 'nil-t2-filing-deadline-ontario', 'nil-t2-filing-deadline-quebec',
	'nil-t2-filing-deadline-british-columbia', 'nil-t2-filing-deadline-alberta', 'nil-t2-filing-deadline-manitoba',
	'nil-t2-filing-deadline-saskatchewan', 'nil-t2-filing-deadline-nova-scotia', 'nil-t2-filing-deadline-new-brunswick',
	'nil-t2-filing-deadline-newfoundland-and-labrador', 'nil-t2-filing-deadline-prince-edward-island', 'nil-t2-filing-deadline-yukon',
	'nil-t2-filing-deadline-northwest-territories', 'nil-t2-filing-deadline-nunavut', 'nil-t2-filing-for-non-resident-owned-corporations-toronto',
	'nil-t2-filing-for-non-resident-owned-corporations-mississauga', 'nil-t2-filing-for-non-resident-owned-corporations-brampton', 'nil-t2-filing-for-non-resident-owned-corporations-scarborough',
	'nil-t2-filing-for-non-resident-owned-corporations-etobicoke', 'nil-t2-filing-for-non-resident-owned-corporations-north-york', 'nil-t2-filing-for-non-resident-owned-corporations-markham',
	'nil-t2-filing-for-non-resident-owned-corporations-vaughan', 'nil-t2-filing-for-non-resident-owned-corporations-richmond-hill', 'nil-t2-filing-for-non-resident-owned-corporations-oakville',
	'nil-t2-filing-for-non-resident-owned-corporations-ottawa', 'nil-t2-filing-for-non-resident-owned-corporations-oshawa', 'nil-t2-filing-for-non-resident-owned-corporations-guelph',
	'nil-t2-filing-for-non-resident-owned-corporations-hamilton', 'nil-t2-filing-for-non-resident-owned-corporations-windsor', 'nil-t2-filing-for-non-resident-owned-corporations-ontario',
	'nil-t2-filing-for-non-resident-owned-corporations-quebec', 'nil-t2-filing-for-non-resident-owned-corporations-british-columbia', 'nil-t2-filing-for-non-resident-owned-corporations-alberta',
	'nil-t2-filing-for-non-resident-owned-corporations-manitoba', 'nil-t2-filing-for-non-resident-owned-corporations-saskatchewan', 'nil-t2-filing-for-non-resident-owned-corporations-nova-scotia',
	'nil-t2-filing-for-non-resident-owned-corporations-new-brunswick', 'nil-t2-filing-for-non-resident-owned-corporations-newfoundland-and-labrador', 'nil-t2-filing-for-non-resident-owned-corporations-prince-edward-island',
	'nil-t2-filing-for-non-resident-owned-corporations-yukon', 'nil-t2-filing-for-non-resident-owned-corporations-northwest-territories', 'nil-t2-filing-for-non-resident-owned-corporations-nunavut',
	);

	$map = array();
	foreach ( $f1 as $s ) { $map[ $s ] = 'F1'; }
	foreach ( $f3 as $s ) { $map[ $s ] = 'F3'; }
	foreach ( $f4 as $s ) { $map[ $s ] = 'F4'; }

	return $map;
}

/**
 * Public helper. Returns the family code ('F1'|'F3'|'F4') or false.
 */
function cnf_is_reserved_slug( $slug ) {
	$map  = cnf_reserved_slugs();
	$slug = sanitize_title( $slug );
	return isset( $map[ $slug ] ) ? $map[ $slug ] : false;
}

/**
 * Hard stop: a page or post may not take a reserved slug.
 */
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

/**
 * REST refusal, so the editor and the Python pipeline both get a real error
 * instead of a silently renamed slug.
 */
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

/**
 * Pre-flight endpoint for the Python pipeline: check before creating, not after.
 *   GET /wp-json/cnf/v1/slug-check?slug=nil-t2-filing-toronto
 */
add_action( 'rest_api_init', 'cnf_register_slug_check' );
function cnf_register_slug_check() {
	register_rest_route( 'cnf/v1', '/slug-check', array(
		'methods'             => 'GET',
		'permission_callback' => function () { return current_user_can( 'edit_posts' ); },
		'args'                => array(
			'slug' => array( 'required' => true, 'type' => 'string' ),
		),
		'callback'            => function ( $request ) {
			$slug   = sanitize_title( $request->get_param( 'slug' ) );
			$family = cnf_is_reserved_slug( $slug );

			return array(
				'slug'     => $slug,
				'reserved' => (bool) $family,
				'family'   => $family ? $family : null,
				'taken_by' => cnf_lookup_root_slug( $slug ) ?: null,
			);
		},
	) );
}

/* ------------------------------------------------------------------ *
 * 5. Flush once per version, never on every load
 * ------------------------------------------------------------------ */

add_action( 'init', 'cnf_maybe_flush_rules', 999 );
function cnf_maybe_flush_rules() {
	if ( get_option( 'cnf_router_version' ) === CNF_ROUTER_VERSION ) {
		return;
	}

	flush_rewrite_rules( false );
	update_option( 'cnf_router_version', CNF_ROUTER_VERSION, false );
}
