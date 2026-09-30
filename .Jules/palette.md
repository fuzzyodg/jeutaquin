## 2026-03-30 - Interactive Cart Controls & Dynamic Announcements Accessibility

**Learning:** Dynamic DOM content rendered from templates (like shopping cart items) often uses non-interactive `<span>` elements or icon-only buttons without ARIA labels, making them inaccessible to keyboard and screen reader users. Additionally, toast messages appended dynamically without `role="status"` and `aria-live="polite"` fail to be announced to assistive technologies.

**Action:**
1. Always use semantic `<button>` elements with descriptive `aria-label` attributes for dynamic actions (e.g., removing items, adjusting quantities).
2. Ensure dynamic toast notifications are initialized with `role="status"` and `aria-live="polite"` so state changes are automatically announced.
