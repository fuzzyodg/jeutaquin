# Palette's Journal

## 2025-05-15 - Accessible Shopping Cart Pattern
**Learning:** In vanilla multi-page architectures, dynamic UI components like shopping carts often suffer from "div-itis" and non-semantic interactions (like `<span>` with `onclick`). This breaks keyboard navigation and screen reader support, as these elements are not focusable or identifiable as actions.
**Action:** Replace non-semantic interactive spans with semantic `<button>` elements. Use `aria-label` for icon-only controls and `aria-live="polite"` on numerical values (quantities, totals) to ensure dynamic updates are announced to assistive technologies.

## 2025-05-15 - Multi-page Navigation Maintenance
**Learning:** Broken internal links (e.g., `accueil.html` vs `index.html`) are common in projects without a centralized router or template engine. This degrades UX through "Page Not Found" errors.
**Action:** When modifying headers or footers in vanilla projects, perform a global search (`grep`) for all navigation labels to ensure consistent destinations and removal of legacy `target="_blank"` attributes for internal links.
