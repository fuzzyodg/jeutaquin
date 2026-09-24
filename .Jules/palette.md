## 2025-05-20 - Dynamic Cart Actions and Live Region Accessibility

**Learning:** Dynamic DOM content generated via JS template strings in multi-page applications often uses non-interactive elements like `<span>` for deletion actions or omits ARIA attributes for quantity buttons. Additionally, dynamically created toast elements lack screen reader announcement capabilities unless `role="status"` and `aria-live="polite"` are explicitly set upon element creation.

**Action:** Always render interactive item controls in JS template literals using semantic `<button type="button">` elements with descriptive `aria-label`s, and ensure dynamic toast containers are initialized with `role="status"` and `aria-live="polite"`.
