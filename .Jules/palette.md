## 2025-05-15 - Cart Accessibility and Event Delegation
**Learning:** Shared UI components in vanilla multi-page architectures (like the shopping cart) require manual synchronization across all HTML files. Non-semantic elements (spans) and inline event handlers (onclick) hinder accessibility and maintainability.
**Action:** Always use semantic `<button>` elements for interactive triggers, implement event delegation on a stable parent, and ensure `aria-live` regions and descriptive `aria-label` attributes are consistently applied across all pages sharing the component.
