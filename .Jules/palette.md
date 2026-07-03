## 2025-05-15 - Event Delegation & Cart Accessibility
**Learning:** In vanilla JS multi-page apps, using event delegation on a persistent container (like `#cart-body`) is significantly more robust than inline `onclick` handlers, especially when content is frequently re-rendered. It also facilitates cleaner HTML templates and safer attribute escaping.
**Action:** Always prefer event delegation for dynamic lists and use `aria-live="polite"` for numerical updates like cart totals to ensure screen reader visibility.

## 2025-05-15 - Static Page Link Consistency
**Learning:** Broken internal links (e.g., `accueil.html` vs `index.html`) often persist in mobile menus of static multi-page sites because they are overlooked during manual updates across files.
**Action:** When updating a shared component like a header or footer in a vanilla project, grep for similar patterns across all `.html` files to ensure synchronization.
