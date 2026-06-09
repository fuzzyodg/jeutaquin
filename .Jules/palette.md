## 2025-05-15 - [Cart UX & Accessibility Refactor]
**Learning:** For dynamic UI components like shopping carts, transitioning from inline `onclick` handlers to a centralized event delegation pattern on a stable parent element (e.g., `#cart-body`) significantly improves code maintainability and allows for more robust accessibility implementation. Using `data-*` attributes to pass context (like item names for `aria-label`) ensures that assistive technologies can provide meaningful feedback even when the UI is generated on the fly.

**Action:** Prefer event delegation for all dynamic list interactions. Always pair visual feedback (like the `.cart-bump` animation) with auditory/textual feedback (`aria-live`, `aria-label`) to ensure a truly inclusive experience.
