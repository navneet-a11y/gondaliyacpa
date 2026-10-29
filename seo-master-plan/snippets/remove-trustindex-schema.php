<?php
/**
 * Change 4: remove the review schema that Trustindex widgets print about our own firm.
 * Strips every <script type="application/ld+json" data-trustindex="1"> block from page output.
 * The review widgets themselves still show; only their schema (AggregateRating, Review,
 * old addresses) is removed. All other JSON-LD on the page is left as is.
 *
 * Install: WPCode Lite > Code Snippets > Add New > PHP Snippet, paste from the line below,
 * Location: "Run Everywhere", then Activate. Purge LiteSpeed afterwards.
 */
add_action( 'template_redirect', function () {
	if ( is_admin() || wp_doing_ajax() || ( defined( 'REST_REQUEST' ) && REST_REQUEST ) ) {
		return;
	}
	ob_start( function ( $html ) {
		if ( strpos( $html, 'data-trustindex' ) === false ) {
			return $html;
		}
		$clean = preg_replace(
			'#<script\b[^>]*\bdata-trustindex=(["\']?)1\1[^>]*>.*?</script>#is',
			'',
			$html
		);
		return ( null === $clean ) ? $html : $clean;
	} );
} );
