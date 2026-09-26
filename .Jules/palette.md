# Palette UX Journal

## 2026-05-20 - Semantic Interactive Elements in Dynamic Cart Templates
**Learning:** Interactive cart actions (like item removal) rendered dynamically via template literals must use semantic `<button>` elements with descriptive `aria-label` attributes instead of non-interactive `<span>` tags with `onclick` handlers, ensuring full keyboard focusability, screen reader announcement, and intuitive user feedback.
**Action:** Always wrap dynamic item actions in semantic `<button>` tags with descriptive ARIA attributes.
