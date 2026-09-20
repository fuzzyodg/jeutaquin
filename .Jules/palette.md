# Palette's UX & Accessibility Journal

## 2026-03-20 - Modal & Toast Accessibility Enhancements
**Learning:** In vanilla HTML/JS applications, interactive overlays like shopping cart sidebars and event modals require global keydown listeners for the `Escape` key to maintain keyboard accessibility, alongside aria-label attributes on close buttons. Dynamic toast elements created in JS also need `role="status"` and `aria-live="polite"` set upon element creation so screen readers announce dynamic notifications.
**Action:** Always ensure close buttons have descriptive `aria-label` attributes, bind `Escape` key listener for modal/overlay dismissal, and set `role="status"` and `aria-live="polite"` when dynamically creating toast notifications.
