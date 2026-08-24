## 2026-08-24 - Event Delegation for Dynamic HTML Cart Items
**Learning:** Using inline `onclick` string handlers in template literals introduces XSS risks and syntax errors when strings contain quotes or apostrophes (e.g. French dish names with `d'`).
**Action:** Always use event delegation on parent container elements (e.g., `#cart-body`) with `data-*` attributes (`data-action`, `data-name`) and semantic `<button>` tags with descriptive `aria-label` attributes.
