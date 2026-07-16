## 2025-05-15 - [Dynamic Cart Accessibility]
**Learning:** For dynamic UI elements that update content without user focus change, such as shopping cart quantities, `aria-live="polite"` is essential to ensure screen reader users are notified of the change without interrupting their flow.
**Action:** Always include `aria-live` on status indicators and use semantic `<button>` elements instead of `<span>` or `<div>` for interactive controls in template literals to ensure keyboard focusability and screen reader recognition.

## 2025-05-15 - [Global Escape Key Pattern]
**Learning:** Users instinctively try to close overlays (modals, sliding panels) with the Escape key. Implementing this globally enhances the "feel" of the app and improves accessibility for keyboard users.
**Action:** Add a global `keydown` listener for 'Escape' when modals are active to provide a consistent dismissal experience.
