# Palette's UX Journal

## 2026-05-20 - Accessible Interactive Cart Elements & Modal Keyboard Dismissal
**Learning:** In vanilla multi-page interfaces with dynamic JavaScript shopping cart renderings, interactive controls such as item removal often default to non-interactive `<span>` tags without labels or focus outlines. Screen readers miss updates without `role="status"` and `aria-live="polite"` on notifications, and keyboard users can get trapped in overlays without an Escape key listener.
**Action:** Always render cart mutations as semantic `<button>` elements with descriptive `aria-label` attributes, sanitize dynamic names with dedicated HTML attribute vs JS escaping, implement global `Escape` listeners for open drawers/modals, and provide standard `:focus-visible` styling using the brand's primary color token.
