## 2025-05-14 - Shopping Cart Delegation & Accessibility
**Learning:** Migrating from inline `onclick` handlers to a single event delegation listener on a stable parent (`#cart-body`) improves both security (avoiding inline script execution) and maintainability. Using semantic `<button>` elements with `aria-label` and `aria-live` significantly improves the experience for screen reader users compared to generic `<span>` or `<div>` tags.
**Action:** Always prefer event delegation for dynamic lists and use semantic interactive elements with appropriate ARIA attributes for all user controls.
