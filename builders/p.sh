#!/bin/sh
# usage: p.sh file.php  -- run PHP file contents via execute-php
sh "$(dirname "$0")/ab.sh" novamira/execute-php "$(python3 -c 'import json,sys;print(json.dumps({"code":open(sys.argv[1]).read()}))' "$1")"
