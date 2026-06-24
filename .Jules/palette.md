# Palette's Journal - A'kadi Restaurant UX/A11y Learnings

## 2025-05-15 - [Dynamic UI Feedback Patterns]
**Learning:** In a vanilla JS environment, providing immediate feedback for asynchronous or DOM-driven actions (like adding to cart) requires both visual and auditory cues. To reliably restart CSS animations (like a "bump" effect) on subsequent clicks, a DOM reflow must be forced between class removals and additions. For accessibility, `aria-live="polite"` is essential for numerical indicators (cart counts) to ensure screen reader users are notified of changes without focus displacement.

**Action:** Always include a "reflow trigger" (e.g., `void element.offsetWidth`) when toggling animation classes in JS. Ensure all dynamic counters have `aria-live` properties defined in the base HTML.
