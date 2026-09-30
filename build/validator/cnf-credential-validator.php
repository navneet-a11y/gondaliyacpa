<?php
/**
 * cnf-credential-validator — corpnilfilingfor300.ca
 *
 * WPCode Lite snippet. PHP Snippet, Run Everywhere, priority 10.
 * Deliverable: Tuesday 29 September 2026.
 *
 * Rule 5: the EFILE number and the CRA GroupID never appear on any page, in any
 * schema block, in any sitemap, image or email.
 *
 * This blocks a save rather than cleaning one up afterwards. It checks title,
 * content, excerpt and every cnf_ meta value on the way in, over REST, which is
 * the path both the block editor and the Python pipeline use.
 *
 * The real credential values are NEVER stored in this file. Put them in
 * wp-config.php instead, where they stay out of the repository and out of any
 * plugin export:
 *
 *     define( 'CNF_EFILE_NUMBER', 'XXXXXX' );
 *     define( 'CNF_CRA_GROUPID',  'XXXXXXXX' );
 *
 * With those defined the match is exact. Without them the pattern rules below
 * still catch the common shapes.
 */

if ( ! defined( 'ABSPATH' ) ) { exit; }

define( 'CNF_VALIDATOR_VERSION', '1.0.0' );

/**
 * Post types the validator guards.
 */
function cnf_guarded_post_types() {
	return array(
		'nil_vertical', 'nil_calculator', 'nil_city_hub', 'nil_service_place',
		'nil_question', 'nil_listicle', 'nil_comparison', 'nil_cost',
		'nil_guide', 'nil_first_filing', 'nil_review_hub', 'nil_case_study',
		'nil_deadline', 'post', 'page',
	);
}

/**
 * Pattern rules. Each returns a human-readable reason when it matches.
 *
 * Label rules are the reliable ones: a credential leaks with its label far more
 * often than as a bare token, and matching the label avoids the false positives
 * a bare six-digit pattern would cause against prices, years and postal codes.
 */
function cnf_credential_rules() {
	return array(
		array(
			'name'    => 'EFILE number with label',
			'pattern' => '/\bE[\s-]?FILE\s*(?:number|no\.?|num\.?|#)\s*[:=]?\s*[A-Z0-9][A-Z0-9-]{3,}/i',
		),
		array(
			'name'    => 'CRA GroupID with label',
			'pattern' => '/\bGroup\s*ID\s*[:=]?\s*[A-Z0-9][A-Z0-9-]{3,}/i',
		),
		array(
			'name'    => 'EFILE-format token (letter followed by five digits)',
			'pattern' => '/\b[A-Z]\d{5}\b/',
		),
	);
}

/**
 * Scan one string. Returns an array of reasons, empty when clean.
 */
function cnf_scan_for_credentials( $text ) {
	$hits = array();

	if ( ! is_string( $text ) || '' === $text ) {
		return $hits;
	}

	// Exact values, when wp-config supplies them.
	foreach ( array( 'CNF_EFILE_NUMBER' => 'EFILE number', 'CNF_CRA_GROUPID' => 'CRA GroupID' ) as $const => $label ) {
		if ( defined( $const ) && constant( $const ) && false !== stripos( $text, constant( $const ) ) ) {
			$hits[] = $label . ' (exact value)';
		}
	}

	foreach ( cnf_credential_rules() as $rule ) {
		if ( preg_match( $rule['pattern'], $text ) ) {
			$hits[] = $rule['name'];
		}
	}

	return array_unique( $hits );
}

/**
 * Scan a whole post payload: title, content, excerpt and every cnf_ meta value.
 */
function cnf_scan_post_payload( $prepared, $request ) {
	$fields = array();

	foreach ( array( 'title', 'content', 'excerpt' ) as $f ) {
		if ( isset( $prepared->{'post_' . $f} ) ) {
			$fields[ $f ] = $prepared->{'post_' . $f};
		}
	}

	$meta = $request->get_param( 'meta' );

	if ( is_array( $meta ) ) {
		foreach ( $meta as $key => $value ) {
			if ( 0 === strpos( $key, 'cnf_' ) && is_scalar( $value ) ) {
				$fields[ 'meta:' . $key ] = (string) $value;
			}
		}
	}

	$found = array();

	foreach ( $fields as $where => $text ) {
		foreach ( cnf_scan_for_credentials( $text ) as $reason ) {
			$found[] = $where . ' — ' . $reason;
		}
	}

	return $found;
}

/**
 * Refuse the write. Applies to the block editor, the REST API and the Python
 * publishing pipeline, since all three come through the same filter.
 */
foreach ( cnf_guarded_post_types() as $cnf_pt ) {
	add_filter( "rest_pre_insert_{$cnf_pt}", 'cnf_block_credential_leak', 10, 2 );
}

function cnf_block_credential_leak( $prepared, $request ) {
	$found = cnf_scan_post_payload( $prepared, $request );

	if ( empty( $found ) ) {
		return $prepared;
	}

	error_log( '[cnf] credential validator blocked a save: ' . implode( '; ', $found ) );

	return new WP_Error(
		'cnf_credential_in_content',
		'Refused: this content matches a credential pattern. ' . implode( '; ', $found )
		. '. The EFILE number and the CRA GroupID must never appear on any page, in any schema block, sitemap, image or email.',
		array( 'status' => 409, 'matches' => $found )
	);
}

/**
 * Meta written outside the post payload is guarded too, so a value cannot be
 * slipped in by a later update_post_meta call.
 */
add_filter( 'update_post_metadata', 'cnf_block_credential_meta', 10, 5 );
function cnf_block_credential_meta( $check, $object_id, $meta_key, $meta_value, $prev_value ) {
	if ( 0 !== strpos( $meta_key, 'cnf_' ) || ! is_scalar( $meta_value ) ) {
		return $check;
	}

	$hits = cnf_scan_for_credentials( (string) $meta_value );

	if ( empty( $hits ) ) {
		return $check;
	}

	error_log( sprintf(
		'[cnf] credential validator blocked meta "%s" on post %d: %s',
		$meta_key, (int) $object_id, implode( '; ', $hits )
	) );

	return false; // short-circuits the write
}

/**
 * Pre-flight for the Python pipeline. Check a candidate block before building,
 * so a bad block fails the build rather than reaching the site.
 *
 *   POST /wp-json/cnf/v1/credential-check   { "text": "..." }
 */
add_action( 'rest_api_init', 'cnf_register_credential_check' );
function cnf_register_credential_check() {
	register_rest_route( 'cnf/v1', '/credential-check', array(
		'methods'             => 'POST',
		'permission_callback' => function () { return current_user_can( 'edit_posts' ); },
		'args'                => array(
			'text' => array( 'required' => true, 'type' => 'string' ),
		),
		'callback'            => function ( $request ) {
			$hits = cnf_scan_for_credentials( $request->get_param( 'text' ) );

			return array(
				'clean'   => empty( $hits ),
				'matches' => array_values( $hits ),
				'version' => CNF_VALIDATOR_VERSION,
			);
		},
	) );
}
