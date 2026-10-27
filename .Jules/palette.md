# Palette's Journal - Critical Learnings

## 2026-03-30 - Interactive Cart Item Controls & Toast Accessibility
**Learning:** In vanilla JS multi-page apps with dynamically rendered cart items, using non-interactive `<span>` elements for actions (like item deletion) breaks keyboard navigation and screen reader accessibility. Dynamic toasts also require `role="status"` and `aria-live="polite"` set upon element creation to reliably trigger screen reader announcements.
**Action:** Always render cart actions as semantic `<button>` elements with descriptive `aria-label` attributes and reset default button styles in CSS. Ensure toast notification containers feature live region attributes upon instantiation.
