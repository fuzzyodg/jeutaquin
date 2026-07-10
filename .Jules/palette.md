# Palette's UX Journal

## 2025-05-14 - Shopping Cart Accessibility & Navigation Consistency
**Learning:** In vanilla multi-page projects, event delegation on dynamic content (like a shopping cart) combined with semantic `<button>` elements and `aria-label` attributes significantly improves both accessibility and code maintainability. Correcting legacy navigation links (`accueil.html` vs `index.html`) is a critical but often overlooked micro-UX fix that prevents 404 errors and user frustration.
**Action:** Always prefer `e.target.closest('button')` with `dataset` metadata for dynamic UI components. Regularly grep for legacy filename patterns across all HTML files to ensure navigation integrity.
