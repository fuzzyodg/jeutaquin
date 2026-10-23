## 2026-10-23 - Accessibility for Dynamic Toast Notifications
**Learning:** Dynamically injected UI notifications (such as shopping cart confirmation toasts created via JavaScript DOM methods) are invisible to screen readers unless configured with explicit ARIA live region attributes.
**Action:** Always set `role="status"` and `aria-live="polite"` on dynamically created toast container elements when initializing them in DOM helpers.
