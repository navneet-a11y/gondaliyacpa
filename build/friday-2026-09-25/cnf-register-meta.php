<?php
/**
 * cnf-register-meta — corpnilfilingfor300.ca
 *
 * WPCode Lite snippet. Type: PHP Snippet. Location: Run Everywhere. Priority: 10.
 *
 * register_meta for every cnf_ key, across the 13 custom post types plus the two
 * natives: post carries Family 13, page carries Families 15 and 16.
 *
 * Every key is single, REST-visible and gated on edit_posts, so the Python
 * pipeline can write title, body, terms and meta in one atomic REST call, and
 * Elementor Pro's Post Custom Field tag and Rank Math's %customfield()% variable
 * both read the same value.
 *
 * Keys derived from Section 4.2 of the plan, remapped onto the 13-type revision.
 */

if ( ! defined( 'ABSPATH' ) ) { exit; }

function cnf_meta_map() {
	return array(
		'nil_vertical' => array( 'cnf_entity_name' => 'string', 'cnf_entity_is_nil' => 'boolean', 'cnf_not_nil_reason' => 'string', 'cnf_price_incl_hst' => 'string', 'cnf_overflow_price_incl_hst' => 'string', 'cnf_last_verified_et' => 'string', 'cnf_reviewer_schema_id' => 'string', 'cnf_primary_keyword' => 'string', 'cnf_internal_links_json' => 'json', 'cnf_update_note' => 'string' ),
		'nil_calculator' => array( 'cnf_calc_type' => 'string', 'cnf_calc_config_json' => 'json', 'cnf_calc_inputs_json' => 'json', 'cnf_calc_rules_json' => 'json', 'cnf_result_copy_json' => 'json', 'cnf_last_verified_et' => 'string', 'cnf_reviewer_schema_id' => 'string', 'cnf_primary_keyword' => 'string' ),
		'nil_city_hub' => array( 'cnf_place_name' => 'string', 'cnf_place_type' => 'string', 'cnf_place_slug' => 'string', 'cnf_child_service_ids_json' => 'json', 'cnf_local_filing_note' => 'string', 'cnf_last_verified_et' => 'string', 'cnf_primary_keyword' => 'string', 'cnf_internal_links_json' => 'json' ),
		'nil_service_place' => array( 'cnf_service_slug' => 'string', 'cnf_place_slug' => 'string', 'cnf_place_name' => 'string', 'cnf_place_type' => 'string', 'cnf_jurisdiction_return' => 'string', 'cnf_provincial_return_name' => 'string', 'cnf_price_incl_hst' => 'string', 'cnf_overflow_price_incl_hst' => 'string', 'cnf_deadline_rule' => 'string', 'cnf_unique_data_block_json' => 'json', 'cnf_last_verified_et' => 'string', 'cnf_primary_keyword' => 'string' ),
		'nil_question' => array( 'cnf_question_text' => 'string', 'cnf_short_answer' => 'string', 'cnf_long_answer' => 'string', 'cnf_last_verified_et' => 'string', 'cnf_reviewer_schema_id' => 'string', 'cnf_primary_keyword' => 'string', 'cnf_internal_links_json' => 'json' ),
		'nil_listicle' => array( 'cnf_list_rows_json' => 'json', 'cnf_published_price_source_date' => 'string', 'cnf_comparison_disclaimer' => 'string', 'cnf_last_verified_et' => 'string', 'cnf_primary_keyword' => 'string' ),
		'nil_comparison' => array( 'cnf_competitor_name' => 'string', 'cnf_competitor_published_price' => 'string', 'cnf_competitor_intake_method' => 'string', 'cnf_our_price_incl_hst' => 'string', 'cnf_feature_rows_json' => 'json', 'cnf_price_checked_on' => 'string', 'cnf_last_verified_et' => 'string' ),
		'nil_cost' => array( 'cnf_price_incl_hst' => 'string', 'cnf_hst_component' => 'string', 'cnf_net_revenue' => 'string', 'cnf_overflow_price_incl_hst' => 'string', 'cnf_included_rows_json' => 'json', 'cnf_excluded_rows_json' => 'json', 'cnf_last_verified_et' => 'string' ),
		'nil_guide' => array( 'cnf_guide_sections_json' => 'json', 'cnf_toc_json' => 'json', 'cnf_reviewer_schema_id' => 'string', 'cnf_last_verified_et' => 'string', 'cnf_child_ids_json' => 'json', 'cnf_primary_keyword' => 'string', 'cnf_update_note' => 'string' ),
		'nil_first_filing' => array( 'cnf_step_rows_json' => 'json', 'cnf_schedule_24_note' => 'string', 'cnf_53_week_rule_note' => 'string', 'cnf_year_end_match_note' => 'string', 'cnf_last_verified_et' => 'string', 'cnf_primary_keyword' => 'string' ),
		'nil_review_hub' => array( 'cnf_place_name' => 'string', 'cnf_trustindex_widget_id' => 'string', 'cnf_review_count_verified_on' => 'string', 'cnf_claim_audit_ref' => 'string', 'cnf_last_verified_et' => 'string' ),
		'nil_case_study' => array( 'cnf_case_years_filed' => 'string', 'cnf_case_jurisdiction' => 'string', 'cnf_case_outcome' => 'string', 'cnf_case_consent_on_file' => 'boolean', 'cnf_case_anonymised' => 'boolean', 'cnf_last_verified_et' => 'string' ),
		'nil_deadline' => array( 'cnf_fiscal_year_end' => 'string', 'cnf_t2_due_date' => 'string', 'cnf_dissolution_due_rule' => 'string', 'cnf_business_day_rule' => 'string', 'cnf_ontario_holiday_list_json' => 'json', 'cnf_last_verified_et' => 'string', 'cnf_update_note' => 'string' ),
		'post' => array( 'cnf_primary_keyword' => 'string', 'cnf_published_et' => 'string', 'cnf_modified_et' => 'string', 'cnf_reviewer_schema_id' => 'string', 'cnf_internal_links_json' => 'json', 'cnf_update_note' => 'string', 'cnf_hero_image_url' => 'string', 'cnf_meta_description' => 'string' ),
		'page' => array( 'cnf_legal_version' => 'string', 'cnf_effective_date_et' => 'string', 'cnf_claim_audit_ref' => 'string', 'cnf_accessibility_conformance' => 'string', 'cnf_last_verified_et' => 'string', 'cnf_hub_children_query_json' => 'json', 'cnf_hub_facet_config_json' => 'json', 'cnf_child_count' => 'integer' ),
	);
}

/**
 * JSON-valued keys are stored as JSON text. sanitize_text_field would mangle
 * them, so validate instead: keep well-formed JSON, drop anything else.
 */
function cnf_sanitize_json( $value ) {
	if ( '' === $value || null === $value ) {
		return '';
	}

	if ( is_array( $value ) || is_object( $value ) ) {
		return wp_json_encode( $value );
	}

	$decoded = json_decode( (string) $value, true );

	if ( JSON_ERROR_NONE !== json_last_error() ) {
		error_log( '[cnf] rejected malformed JSON meta value' );
		return '';
	}

	return wp_json_encode( $decoded );
}

add_action( 'init', 'cnf_register_all_meta', 20 );
function cnf_register_all_meta() {
	$auth = function () { return current_user_can( 'edit_posts' ); };

	foreach ( cnf_meta_map() as $post_type => $keys ) {
		foreach ( $keys as $key => $kind ) {

			switch ( $kind ) {
				case 'boolean':
					$args = array( 'type' => 'boolean', 'default' => false, 'sanitize_callback' => 'rest_sanitize_boolean' );
					break;

				case 'integer':
					$args = array( 'type' => 'integer', 'default' => 0, 'sanitize_callback' => 'absint' );
					break;

				case 'json':
					$args = array( 'type' => 'string', 'default' => '', 'sanitize_callback' => 'cnf_sanitize_json' );
					break;

				default:
					$args = array( 'type' => 'string', 'default' => '', 'sanitize_callback' => 'sanitize_text_field' );
			}

			register_post_meta( $post_type, $key, array_merge( $args, array(
				'single'        => true,
				'show_in_rest'  => true,
				'auth_callback' => $auth,
			) ) );
		}
	}
}
