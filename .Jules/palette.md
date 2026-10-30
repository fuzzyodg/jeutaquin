## 2026-10-30 - Modal & Overlay Dismissal via Escape Key
**Learning:** Overlays and modals (Shopping Cart panel, Event modal, and Mobile Navigation menu) must support dismissal via the 'Escape' key for enhanced keyboard accessibility and micro-UX consistency across vanilla multi-page web applications.
**Action:** Always include a global keydown listener for the 'Escape' key that cleanly closes all active modal/overlay components and resets `document.body.style.overflow`.
