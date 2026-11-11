#!/bin/sh
# clear Elementor CSS/element caches; the site's sync helper then purges xSpeed page cache
sh "$(dirname "$0")/ab.sh" novamira/execute-php '{"code":"\\Elementor\\Plugin::$instance->files_manager->clear_cache(); if (has_action(\"shutdown\",\"dd_xspeed_purge_now\")===false && function_exists(\"dd_xspeed_purge_now\")) dd_xspeed_purge_now(); return \"ok\";"}'
