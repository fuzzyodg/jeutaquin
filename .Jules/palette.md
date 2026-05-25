## 2025-05-14 - Accessible Slider Navigation & Dynamic Cart Events

**Learning:** Using non-semantic elements like `<span>` for interactive slider navigation prevents keyboard accessibility and screen reader support. Additionally, inline `onclick` handlers on dynamic content (like shopping cart items) violate modern security standards and are harder to maintain than event delegation.

**Action:** Always use `<button>` elements with descriptive `aria-label` for slider indicators. For dynamic lists like a shopping cart, use event delegation on a stable parent element instead of injecting inline event handlers into the HTML string.
