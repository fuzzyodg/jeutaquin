## 2025-05-18 - Centralized Escape Key Handler for Multi-Page Overlays
**Learning:** In vanilla multi-page architectures with disparate drawer/modal state mechanisms (`.cart-panel.active`, `.nav-mobile--active`, `#event-modal.active`), a single global `keydown` event listener in `script.js` cleanly handles keyboard dismissal without individual component event duplication.
**Action:** Check all modal and slide-out overlay implementations in shared scripts for `Escape` key handlers before adding isolated component event listeners.
