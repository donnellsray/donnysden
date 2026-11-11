# Build log

What was built, in order, and why. This is condensed from the live log kept during the build. Page and template IDs refer to the WordPress install.

## Timeline

| Date (2026) | Work |
| --- | --- |
| Oct 1 | Connected Claude Code to the WordPress site through the Novamira MCP server |
| Oct 6 | Recon, global styles, room shell, Front Door, all seven rooms, interactions, QA, prototype match pass, "Come inside" entrance, phone spacing, cache fix, Hallway content, ACF Projects, Coming Soon mode |
| Oct 7 | Font change to Bricolage Grotesque + Figtree; share image re-rendered |
| Oct 8 | Office became the professional About page; Hallway removed and its personal content moved to the Living Room |
| Nov 11 | Reconnected after a cloud container reset; built the Links page (link in bio + Featured Content portfolio) |

## Phase 0: recon and decisions

- **Starting point:** WordPress 7.1, PHP 8.3, LiteSpeed on xCloud, Twenty Twenty-Five theme, Elementor + Elementor Pro 4.3, Novamira, xSpeed Cache. Search engines blocked.
- **Decisions by Donnell:** build directly on production (he takes backups in xCloud); switch to Hello Elementor; the Study is the WordPress Posts page at `/blog/`; build the whole first pass in one go, then review.
- **Contrast:** the prototype's 56% glass gave 2.8–4.1:1 text contrast over bright photos. Raised to 72%, which gives about 6.7 / 5.0 / 4.4:1.

## Phase 1: global styles

- Colors, fonts and the 900px tablet breakpoint set in Elementor Site Settings.
- Shared look as **Global Classes**: `dd-glass`, `dd-surface`, `dd-btn-*`, `dd-chip`, `dd-selected`, `dd-room-title`, `dd-welcome`, `dd-small`, `dd-wordmark` and more.
- One **Custom Code** snippet for what Elementor can't express: tokens, focus ring, blur fallback, reduced motion.
- Placeholder room backgrounds rendered from the prototype's gradients as 2400×1350 WebP files of about 10 KB each.

**Issues found and fixed**

- Atomic containers ship with 10px padding. Every container now sets padding 0 explicitly.
- Global Classes print in list order, so `dd-selected` lost to `dd-chip`. One CSS rule makes selected always win.
- Novamira rejects custom HTML attributes on atomic elements, so ARIA states are set at runtime by the shell script.

## The room shell

Four Theme Builder templates share one look, so each room page holds only its own content:

| Template | Holds |
| --- | --- |
| Den shell: frame | Full-screen background (the page's featured image), glass sidebar, mobile top chip with Hide UI |
| Den shell: room window | The glass window with the page's own Elementor content |
| Den shell: Study window | The same window for the Posts page, which uses an archive template |
| Den shell: ornament, mobile bar, Rooms sheet | Floating pill (Hide UI, previous, room, next), phone bottom bar, "Where to?" sheet |

Every shell piece is `position: fixed`. At 900px and below the sidebar and pill hide, the top chip and bottom bar appear, and the window becomes a sheet. The page never scrolls; the window scrolls inside.

## Front Door, rooms and dialogs

- **Front Door** (Elementor Canvas): porch background, glass panel, "Come inside" and "Ring the doorbell".
- **Doorbell** and **Porch Light** are Elementor Pro popups with reason pills, a budget field only for brand collabs, focus trapping and Escape to close. On phones they become bottom sheets.
- **Living Room:** Now Showing feature, "New around the house" tiles, chips that switch between rows of cards.
- **Other rooms:** title, welcome line, "Step inside" button and an "Inside this room" grid that glides down to each section.

## Interactions

All behavior lives in two snippets: [`snippets/shell-css.html`](../snippets/shell-css.html) and [`snippets/shell-js.html`](../snippets/shell-js.html).

| Interaction | How it works |
| --- | --- |
| Room-to-room crossfade | Cross-document View Transitions; the background crossfades while the shell stays put |
| "Come inside" | Panel fades out, porch crossfades into the Living Room, sidebar slides in, window arrives last. The Living Room is prerendered with speculation rules so it feels instant |
| Hide UI | Fades the shell; remembered for the browser session |
| Previous / next | Read from the sidebar's room order, so reordering rooms needs no code changes |
| Dialogs | `role=dialog`, focus trap, Escape, focus returns to the trigger |
| All my links (Links page) | A real button with `aria-expanded`; the list simply shows without JavaScript |
| Reduced motion | No crossfade, arrival or fades |

## QA

- 8 pages × 5 widths (1440, 1280, 1024, 768, 390): no sideways scroll, no script errors, window exactly where specified.
- All tap targets 44px or more; logical keyboard order; amber focus ring visible.
- Lighthouse mobile: Front Door 75–86 performance, 100 accessibility, 100 best practices; Living Room 70–71 / 100 / 100. SEO scores 61 only because search engines are blocked before launch.

## Fixes worth noting

- **Unstyled pages on a phone.** xSpeed had cached HTML pointing at Elementor CSS files that had since been regenerated. Fix: a small helper ([`mu/dd-elementor-xspeed-sync.php`](../mu/dd-elementor-xspeed-sync.php)) purges the page cache whenever Elementor regenerates CSS or a template, snippet or kit is saved.
- **Phone spacing.** iOS counts hidden toolbars in full-screen height. The Front Door is sized to the visible screen (`dvh`), and the room sheet starts at 84px.

## Content and structure changes

- **Coming Soon mode:** visitors see "The Den opens soon." with an email signup; logged-in users see the real site.
- **Fonts:** Newsreader + Hanken Grotesk became Bricolage Grotesque (headlines) + Figtree (body) across every class, page and template.
- **About:** the Office became the professional About page at `/about/`. The Hallway was removed, and its Right now list and links moved to the Living Room.

## Links page

- `/links/` is a standalone glass page for link-in-bio use, and it stays public during Coming Soon ([`mu/dd-links-public.php`](../mu/dd-links-public.php)).
- Photo, bio, email signup (the same list as Coming Soon), an "All my links" fold-out with 8 links, and **Featured Content**.
- Featured Content is an Elementor Loop Grid of the ACF **Projects** post type. Each card shows a thumbnail, type, title and external link. Adding a project in WordPress adds a card. Order follows publish date.
- Saving a project refreshes the page cache automatically.

## Working with AI: what helped

- **A written brief with ground rules** ("everything editable in Elementor", "custom code in one place", "ask before installing plugins") kept every decision consistent.
- **Verification after every change:** screenshots at phone and desktop sizes, keyboard tests and console checks caught layout bugs before Donnell saw them.
- **Small, reversible steps:** pages went to the trash rather than being deleted, and each change was logged.
- **Limits hit:** Instagram blocks automated image downloads, so thumbnails were uploaded by hand. A cloud container reset wiped local scripts mid-project, and only the most recent builders survive here. The WordPress login moved into an encrypted environment secret.
