## 2025-05-15 - [Dataset Auto-decoding & Animation Reflow]
**Learning:** When using event delegation with `data-*` attributes (e.g., `data-name="L&apos;Atiéké"`), modern browsers automatically decode HTML entities when accessed via the `dataset` property. Manual `.replace()` calls are redundant and can introduce bugs. Additionally, reliably restarting a CSS animation on an element (like a 'cart-bump') requires a DOM reflow (e.g., `void element.offsetWidth`) between removing and re-adding the class.
**Action:** Use `element.dataset` directly for data retrieval without manual entity decoding. Use the `void element.offsetWidth` trick for any repeated interaction-based animations.

## 2025-05-15 - [Aria-Live and Dynamic Cart Updates]
**Learning:** Simply updating numbers in the DOM doesn't notify screen reader users of the change. Adding `aria-live="polite"` to the container ensures that as users interact with the cart (adding/removing items), the changes are announced without interrupting their flow.
**Action:** Always wrap dynamic numerical indicators (cart counts, quantities, prices) in elements with `aria-live="polite"`.
