#!/bin/sh
# usage: ab.sh <ability> '<json params>'  -- runs a Novamira ability through the site's MCP adapter (login injected by the proxy)
U=https://donnysden.1wp.site/wp-json/mcp/mcp-adapter-default-server
D=$(dirname "$0"); SF="$D/.mcp-sid"
init() { H=$(mktemp); curl -sS -D "$H" -o /dev/null -X POST -H 'Content-Type: application/json' -H 'Accept: application/json, text/event-stream' "$U" -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"dd","version":"1"}}}'; grep -i mcp-session-id "$H" | cut -d' ' -f2 | tr -d '\r' > "$SF"; rm -f "$H"; }
[ -s "$SF" ] || init
BODY=$(python3 -c 'import json,sys;print(json.dumps({"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"mcp-adapter-execute-ability","arguments":{"ability_name":sys.argv[1],"parameters":json.loads(sys.argv[2])}}}))' "$1" "${2:-{\}}")
call() { curl -sS -X POST -H 'Content-Type: application/json' -H 'Accept: application/json, text/event-stream' -H "Mcp-Session-Id: $(cat "$SF")" -H 'MCP-Protocol-Version: 2025-06-18' "$U" --data-binary "$BODY"; }
R=$(call); case "$R" in *"ession"*"not found"*|*"nvalid session"*) init; R=$(call);; esac
printf '%s' "$R" | python3 -c 'import json,sys;d=json.load(sys.stdin);r=d.get("result",d);c=r.get("content") if isinstance(r,dict) else None;print(c[0]["text"] if c else json.dumps(r))'
