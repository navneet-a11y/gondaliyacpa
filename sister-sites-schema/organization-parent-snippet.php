<?php
/**
 * WPCode Lite snippet: add parentOrganization to Rank Math's sitewide Organization node.
 * Sites: opencorporationfor35.ca and corpnilfilingfor300.ca (same code on both).
 * Code type: PHP Snippet. Insert method: Auto Insert. Location: Run Everywhere.
 *
 * sameAs gondaliyacpa.ca sits on the parent node, so the brand is not
 * declared to be the same entity as gondaliyacpa.ca.
 * The parent @id matches the @id used on gondaliyacpa.ca.
 */
add_filter( 'rank_math/json_ld', function ( $data, $jsonld ) {
	$parent = array(
		'@type'      => 'Organization',
		'@id'        => 'https://gondaliyacpa.ca/#organization',
		'name'       => 'Gondaliya CPA Professional Corporation',
		'url'        => 'https://gondaliyacpa.ca/',
		'identifier' => 'CPA Ontario Firm ID 61330051',
		'sameAs'     => array( 'https://gondaliyacpa.ca/' ),
	);
	foreach ( $data as $key => $node ) {
		if ( is_array( $node ) && isset( $node['@id'] ) && '/#organization' === substr( $node['@id'], -14 ) ) {
			$data[ $key ]['parentOrganization'] = $parent;
		}
	}
	return $data;
}, 99, 2 );
