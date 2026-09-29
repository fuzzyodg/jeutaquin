## 2026-09-29 - Accessible Dynamic Cart Controls & Modal Dismissal

**Learning:** Dynamic DOM content rendered via template literals (like shopping cart items) often loses keyboard accessibility and screen-reader context if non-semantic elements (`<span>`) or unlabelled buttons are used. Adding explicit `aria-label`s, semantic `<button>` elements, escaping quotes in string attributes, and supplying a global `Escape` key listener for drawers/modals drastically improves accessibility without altering layout styles.
**Action:** Always replace `<span>` action controls with semantic `<button>` tags, escape attribute strings for double-quotes, and add `role="status"` / `aria-live="polite"` to toast elements.
