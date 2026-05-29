## 2025-05-24 - [Accessible Cart & Navigation Polish]
**Learning:** Transitioning from inline event handlers to event delegation not only improves code maintainability but also centralizes the management of accessibility attributes like `aria-label` for dynamic content.
**Action:** Always prefer event delegation for dynamic lists (like cart items) and ensure all icon-only buttons have descriptive ARIA labels at the template level.

**Learning:** Internal navigation links using `target="_blank"` break the user's mental model of a single-page session and create unnecessary browser clutter.
**Action:** Audit all internal links to ensure they open in the same tab for a seamless experience.
