# Palette's Journal - Critical UX/A11y Learnings

## 2025-05-15 - [A11y] Semantic Action Triggers in Dynamic UI
**Learning:** Using `<span>` or `<div>` for interactive actions (like 'Remove' or 'Change Quantity') breaks screen reader navigation and keyboard support. Even with ARIA roles, they lack default button behaviors. Reusing semantic `<button>` elements with `aria-label` provides a consistent, accessible experience across the app without extra JS for keydown handling.
**Action:** Always prefer `<button>` over `<span>` for clickable actions. Use `aria-label` for icon-only buttons to ensure context is provided to screen readers.

## 2025-05-15 - [UX] Reliable Animation Triggers for Feedback
**Learning:** When providing visual feedback (like the cart bump animation), simply toggling a CSS class in JavaScript often fails to replay the animation if the user clicks rapidly.
**Action:** Trigger a DOM reflow by accessing `element.offsetWidth` (or similar) between removing and re-adding the animation class to force the browser to restart the animation sequence.

## 2025-05-15 - [UX] Closing the "Dead End" Empty State
**Learning:** An empty shopping cart is a "dead end" if it only contains a close button. It interrupts the shopping flow and forces the user to find the close button and then navigate back to the menu manually.
**Action:** Include a clear "Voir le menu" (View Menu) call-to-action within the empty cart state that automatically closes the cart panel, reducing friction and guiding the user back to the primary conversion path.
