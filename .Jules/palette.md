## 2025-05-20 - Accessible Toasts and Keyboard Overlay Dismissal
**Learning:** Dynamic toast notifications created in JS need `role="status"` and `aria-live="polite"` so screen readers announce shopping cart actions automatically. Additionally, overlays and modals (like cart sliding panel and event modals) must listen for the Escape key to satisfy WCAG keyboard navigation standards.
**Action:** Always set `role="status"` and `aria-live="polite"` on dynamic notification elements upon creation, and bind a global keydown handler for `Escape` on custom overlay UI components.
