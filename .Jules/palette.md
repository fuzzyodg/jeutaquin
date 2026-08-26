# Palette's Journal - Critical Learnings

## 2026-08-26 - Keyboard Overlay Dismissal and ARIA Close Labels
**Learning:** Vanilla HTML multi-page applications with dynamic side panels (shopping cart) and modals often miss global `Escape` key listeners and `aria-label` attributes on icon-only close buttons (e.g. `✕` or `&times;`), leaving screen-reader and keyboard users stranded.
**Action:** Always register a central `Escape` key event listener in `script.js` to dismiss active overlays/modals and ensure all icon close buttons carry explicit `aria-label` attributes across all HTML templates.
