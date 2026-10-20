<?php
/**
 * Adds MBOT membership to the existing Rank Math Organization node
 * (@id https://gondaliyacpa.ca/#organization). Does not add a new node.
 * WPCode > Add Snippet > PHP Snippet, Run Everywhere, Active.
 */
add_filter( 'rank_math/json_ld', function ( $data, $jsonld ) {
	foreach ( $data as $key => $node ) {
		if ( ! is_array( $node ) || empty( $node['@id'] ) ) {
			continue;
		}
		if ( 'https://gondaliyacpa.ca/#organization' !== $node['@id'] ) {
			continue;
		}
		$data[ $key ]['memberOf'] = array(
			'@type' => 'Organization',
			'name'  => 'Mississauga Board of Trade',
			'url'   => 'https://mbot.com/',
		);
	}
	return $data;
}, 99, 2 );
