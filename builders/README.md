# Builders

Scripts used to build and check the site. Run them from this folder.

| File | What it does |
| --- | --- |
| `ab.sh` | Calls one Novamira ability on the site through its MCP endpoint. The WordPress login is added by the environment's network proxy, never stored here |
| `p.sh` | Runs a PHP file on the site through Novamira's PHP ability |
| `flush.sh` | Clears Elementor's CSS cache; the site's sync helper then purges the page cache |
| `dd.py` | Shared helpers that describe Elementor v4 atomic elements (boxes, headings, buttons, images, glass classes) as data |
| `links.py` | Builds the Links page and pushes it to the site |
| `login.py` | Creates a one-time admin login link for screenshot checks (the link is written to `login.json`, which is git-ignored) |
| `snap.mjs`, `toggle.mjs` | Playwright checks: screenshots, sideways-scroll and font checks, and the "All my links" toggle test |
| `data/coming-soon-template.json` | The Coming Soon page's Elementor data; `links.py` reuses its signup form |

The builders for the earlier rooms were lost when the cloud container was reset partway through the project; the live pages remain the source of truth.
