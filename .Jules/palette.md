## 2025-05-22 - Accessible Cart & Micro-interactions
**Learning:** In dynamically generated UIs like shopping carts, replacing inline `onclick` with event delegation not only improves security and maintainability but also simplifies the injection of accessibility attributes (like `aria-label`) that depend on item state.
**Action:** Use event delegation for all dynamic lists and ensure numeric updates use `aria-live="polite"` for immediate screen reader feedback.
