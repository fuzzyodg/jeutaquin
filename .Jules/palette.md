# Palette's Journal - A'kadi Restaurant

## 2025-05-22 - Shopping Cart Accessibility & Navigation Consistency

**Learning:** Internal navigation links in multi-page vanilla projects often suffer from legacy errors like 'accueil.html' (should be 'index.html') or 'evenements.html' (should be 'evenement.html'), and unnecessary 'target="_blank"' attributes which break the flow. Additionally, interactive components like shopping carts often use non-semantic elements and inline 'onclick' handlers, which harm accessibility and maintainability.

**Action:** Standardize navigation links across all HTML files using grep to find and fix legacy paths. Refactor interactive components to use semantic elements (buttons), ARIA labels, and event delegation instead of inline handlers for better accessibility and security.
