# Palette's Journal - Critical UX Learnings

## 2026-08-18 - Global Escape Key Handler for Overlay Panels & Modals
**Learning:** In vanilla multi-page web applications with sliding panels (like shopping cart drawers) and pop-up modals, users expect standard keyboard shortcuts (`Escape` key) to dismiss active overlays, improving keyboard navigation and accessibility.
**Action:** Always register a global `keydown` event listener for `Escape` key that checks for active modal/overlay classes (e.g. `cart-panel.open`, `event-modal.active`) and triggers their close handler to reset body scroll (`overflow = ''`).
