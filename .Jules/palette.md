## 2025-05-20 - ARIA Live Region for Dynamic Toast Notifications & Escape Key Modal Dismissal
**Learning:** Dynamically injected toast notifications (like cart feedback) are silent to screen readers unless configured with `role="status"` and `aria-live="polite"`. In addition, modal overlays and drawer panels must handle the `Escape` key event globally to provide expected keyboard navigation standards.
**Action:** Always ensure dynamically generated UI feedback elements include appropriate ARIA live attributes upon creation, and attach a global `Escape` key listener for open modals/panels.
