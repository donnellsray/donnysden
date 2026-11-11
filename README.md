# Donny's Den

My personal website, designed as a house you walk through. You knock at the **Front Door**, step inside, and move room by room: the Living Room for what's new, the Office for my professional side, the Screening Room for my work, the Study for writing, the Kitchen for things I make and sell, and the Backyard for community.

The whole build was made with AI. I directed it and made the decisions, and [Claude Code](https://claude.ai/code) did the building on a live WordPress site through MCP. This repo documents how.

> **Status:** in progress. Visitors currently see a "The Den opens soon" page with an email signup. The [links page](https://donnysden.1wp.site/links/) is live.

## What's in the house

| Room | Path | What it holds |
| --- | --- | --- |
| Front Door | `/` | The entrance. "Come inside" fades into the Living Room |
| Living Room | `/living-room/` | Now Showing, what's new around the house, Right now, and all my links |
| Office | `/about/` | Professional about: bio, what I do, experience and education, work with me |
| Screening Room | `/portfolio/` | Portfolio (Projects) |
| Study | `/blog/` | Blog |
| Kitchen | `/shop/` | Shop |
| Backyard | `/community/` | Community, Discord and events |
| Links | `/links/` | Link in bio plus Featured Content, my portfolio in a two-column grid |

## Design

- **Look:** glass panels over warm "porch light" scenes, in the spirit of visionOS. Headlines are set in Bricolage Grotesque and body text in Figtree.
- **Layout:** a fixed shell (sidebar, room window and a floating control pill on desktop; a top bar, bottom bar and Rooms sheet on phones) wraps every room. Prev and next arrows walk the rooms in menu order.
- **Rule one:** everything I'd edit later (text, buttons, links, images, room labels) stays editable in Elementor. Custom CSS and JS are only for the shared shell and its interactions, and they live in one place.
- **Accessibility:** keyboard focus traps in dialogs, Escape to close, real buttons and ARIA states, skip link, reduced-motion support and 44px tap targets.

## Stack

- **WordPress** with the **Hello Elementor** theme
- **Elementor Pro**: v4 atomic elements, Global Classes, Theme Builder, Loop Grid, Forms, Popups and Custom Code
- **ACF** for the `project` post type, which feeds Featured Content and the Screening Room
- **xCloud** hosting with xSpeed page cache
- **Claude Code**, working through the **Novamira** MCP server to read and edit the site

## How it was built with AI

1. **Brief first.** I wrote the concept, rooms, ground rules and quality bar, then shared a clickable prototype.
2. **Claude Code connected to WordPress** through the Novamira MCP server, using an application password. It worked on the real site through structured "abilities" (create pages, set Elementor content, manage global classes, run checks) rather than by pasting code into an editor.
3. **Pages were generated as data.** Small Python builders describe each room as an Elementor element tree, with shared helpers for glass panels, buttons and tiles, and push it to the site. Rebuilding a room is one command.
4. **Every change was verified.** After each step Claude took headless-browser screenshots at phone and desktop sizes, checked for horizontal scroll, console errors, font loading and keyboard behavior, and ran Lighthouse.
5. **One decision at a time.** I approved each phase, supplied the content (links, bio, projects, photos) and steered the design. Claude kept a running build log of every change.

## Repo layout

```
snippets/      the shared shell CSS and JS (Elementor > Custom Code), the only custom code on the site
mu/            small helper plugins: page-cache sync, keeping /links/ public during coming soon
builders/      Python scripts that generate each room's Elementor layout
docs/          build log and decisions
```

No credentials, passwords or API keys are stored in this repo.

## Credits

Concept, content and direction by **Donnell Ray** ([@donnellsray](https://www.instagram.com/donnellsray/)).
Built with [Claude Code](https://claude.ai/code).
