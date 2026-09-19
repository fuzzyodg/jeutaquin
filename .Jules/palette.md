# Palette's Journal - A'kadi Restaurant

## 2026-09-19 - Global Escape Key Modal Dismissal & Modal Close ARIA Labels
**Learning:** In vanilla HTML/JS multi-page web applications with drawer overlays (cart panel) and modal dialogs (events modal), modal overlays often lack keyboard Escape listeners and ARIA labels on close buttons. Adding a centralized keydown listener for the `Escape` key in the shared `script.js` ensures keyboard accessibility across all pages without duplicating handlers.
**Action:** Always check shared UI components for `Escape` key dismissal and ensure `aria-label` is explicitly set on icon-only close buttons (`✕`, `×`).
