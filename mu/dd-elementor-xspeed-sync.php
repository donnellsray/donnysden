<?php
/**
 * Donny's Den: keep the xSpeed page cache in step with Elementor's CSS files.
 *
 * When Elementor regenerates its shared CSS (Global Classes, kit, templates),
 * old CSS files disappear. Pages already in the xSpeed cache still point at
 * them, so visitors get an unstyled page. This empties the page cache once,
 * at the end of any request where Elementor cleared CSS or a shared document
 * (template, popup, kit) was saved.
 */
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function dd_xspeed_purge_later() {
	static $queued = false;
	if ( $queued ) {
		return;
	}
	$queued = true;
	add_action( 'shutdown', 'dd_xspeed_purge_now', 1 );
}

function dd_xspeed_purge_now() {
	global $wp_filter;
	foreach ( $wp_filter as $hook ) {
		foreach ( $hook->callbacks as $callbacks ) {
			foreach ( $callbacks as $cb ) {
				if ( is_array( $cb['function'] ) && is_object( $cb['function'][0] ) && $cb['function'][0] instanceof \XSpeed\Cache ) {
					$cb['function'][0]->purge_all();
					return;
				}
			}
		}
	}
}

add_action( 'elementor/core/files/clear_cache', 'dd_xspeed_purge_later' );
add_action( 'elementor/atomic-widgets/styles/clear', 'dd_xspeed_purge_later' );
add_action( 'save_post_elementor_library', 'dd_xspeed_purge_later' );
add_action( 'save_post_elementor_snippet', 'dd_xspeed_purge_later' );
add_action( 'update_option_elementor_active_kit', 'dd_xspeed_purge_later' );
add_action( 'update_option_elementor_maintenance_mode_mode', 'dd_xspeed_purge_later' );
add_action( 'update_option_elementor_maintenance_mode_template_id', 'dd_xspeed_purge_later' );
