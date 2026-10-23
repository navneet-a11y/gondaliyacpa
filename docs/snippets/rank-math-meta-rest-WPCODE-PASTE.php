/*
 * Exposes Rank Math's SEO title, meta description, focus keyword and canonical
 * to the WordPress REST API, so they can be set programmatically.
 *
 * rank_math_robots is NOT exposed on purpose. It holds the site-wide noindex
 * that hard rule 10 depends on until launch, and leaving it unwritable means no
 * automated edit can flip it by accident. Set that one by hand in Rank Math.
 *
 * Named functions, not closures, and every declaration is guarded with
 * function_exists so the snippet is safe if it ever loads twice.
 */

if ( ! function_exists( 'cnf_rank_math_meta_keys' ) ) {
	function cnf_rank_math_meta_keys() {
		return array(
			'rank_math_title',
			'rank_math_description',
			'rank_math_focus_keyword',
			'rank_math_canonical_url',
		);
	}
}

if ( ! function_exists( 'cnf_rank_math_post_types' ) ) {
	function cnf_rank_math_post_types() {
		return array(
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
	}
}

if ( ! function_exists( 'cnf_rank_math_meta_sanitize' ) ) {
	function cnf_rank_math_meta_sanitize( $value ) {
		return wp_strip_all_tags( (string) $value );
	}
}

if ( ! function_exists( 'cnf_rank_math_meta_auth' ) ) {
	function cnf_rank_math_meta_auth( $allowed, $meta_key, $post_id ) {
		return current_user_can( 'edit_post', $post_id );
	}
}

if ( ! function_exists( 'cnf_rank_math_register_rest_meta' ) ) {
	function cnf_rank_math_register_rest_meta() {

		$post_types = cnf_rank_math_post_types();
		$meta_keys  = cnf_rank_math_meta_keys();

		$args = array(
			'type'              => 'string',
			'single'            => true,
			'show_in_rest'      => true,
			'sanitize_callback' => 'cnf_rank_math_meta_sanitize',
			'auth_callback'     => 'cnf_rank_math_meta_auth',
		);

		foreach ( $post_types as $post_type ) {
			foreach ( $meta_keys as $meta_key ) {
				register_post_meta( $post_type, $meta_key, $args );
			}
		}
	}
}

/* Priority 20 so this runs after Rank Math registers its own meta. */
add_action( 'init', 'cnf_rank_math_register_rest_meta', 20 );
