# Palette's Journal - UX & Accessibility Learnings

## 2026-05-21 - [Accessibility patterns for icon-only buttons]
**Learning:** Icon-only buttons (like cart controls or close buttons) are invisible to screen readers if they lack descriptive `aria-label` attributes. Standardizing these across the app ensures a consistent and accessible experience.
**Action:** Always verify that every interactive icon has a corresponding `aria-label` and avoid inline `onclick` handlers in favor of event delegation for better maintainability and security.
