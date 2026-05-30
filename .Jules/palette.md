## 2025-03-24 - [Cart Interaction & Accessibility]
**Learning:** In vanilla JavaScript applications with dynamic DOM injection, it is crucial to use event delegation instead of inline `onclick` handlers. This ensures that new elements (like cart items) are automatically interactive without re-binding listeners. Additionally, dynamic content often misses semantic roles and ARIA labels, which are essential for screen reader users to understand quantity controls and removal actions.

**Action:** Always prefer `addEventListener` on a stable parent element. Ensure all dynamic interactive elements have descriptive `aria-label` attributes and use semantic `<button>` tags instead of `<span>` or `<a>` for actions.

## 2025-03-24 - [Feedback & Flow]
**Learning:** Interactive components like side-panels (carts) can feel "disconnected" from the main content if they don't provide immediate feedback upon external actions (like clicking "Ajouter" on a separate page section). A subtle "bump" or "pulse" animation on the cart trigger provides immediate visual confirmation of the action. Furthermore, an empty cart state is a dead-end without a clear Call To Action (CTA).

**Action:** Implement micro-animations (e.g., CSS transforms) to acknowledge user actions. Always provide a "recovery" path (like a "View Menu" link) in empty states to maintain user flow.
