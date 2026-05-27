# Palette's UX Journal - A'kadi Restaurant

This journal tracks critical UX and accessibility learnings discovered during the development of the A'kadi Restaurant website.

---

## 2025-05-27 - Secure Attribute Injection in Shopping Cart
**Learning:** Removing attribute escaping (like `esc()`) when migrating from inline handlers to event delegation can lead to DOM corruption if data contains special characters (e.g., quotes in restaurant dish names). Always use a robust escaping function like `escAttr()` for any dynamic content injected into HTML attributes, especially `data-*` and `aria-label`.
**Action:** Implement `escAttr()` for all dynamic template literals injected into the DOM and ensure it handles `&`, `<`, `>`, `"`, and `'`.
