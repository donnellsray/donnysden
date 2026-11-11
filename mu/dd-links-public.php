<?php
// Donny's Den: keep /links/ public while Elementor's coming soon mode covers the rest of the site.
add_action('template_redirect', function () {
	if (!is_page('links')) return;
	global $wp_filter;
	if (empty($wp_filter['template_redirect'])) return;
	foreach ($wp_filter['template_redirect']->callbacks as $prio => $cbs) {
		foreach ($cbs as $cb) {
			$fn = $cb['function'];
			if (is_array($fn) && is_object($fn[0]) && substr(get_class($fn[0]), -16) === 'Maintenance_Mode') {
				remove_action('template_redirect', $fn, $prio);
			}
		}
	}
}, 1);
// Refresh the page cache when a project (Featured content work) is saved or its thumbnail changes.
add_action('save_post_project', function () { if (function_exists('dd_xspeed_purge_later')) dd_xspeed_purge_later(); });
add_action('updated_post_meta', function ($mid, $pid, $key) { if ($key === '_thumbnail_id' && get_post_type($pid) === 'project' && function_exists('dd_xspeed_purge_later')) dd_xspeed_purge_later(); }, 10, 3);
add_action('added_post_meta', function ($mid, $pid, $key) { if ($key === '_thumbnail_id' && get_post_type($pid) === 'project' && function_exists('dd_xspeed_purge_later')) dd_xspeed_purge_later(); }, 10, 3);
