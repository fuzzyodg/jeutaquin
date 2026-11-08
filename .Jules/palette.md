# Palette's Journal

## 2026-05-20 - Accessible Cart Item Controls & Dynamic Live Announcements
**Learning:** In vanilla multi-page client-side shopping carts, generating dynamic HTML via template literals often leads to using non-semantic elements (`<span>` with `onclick`) for destructive actions like item removal, which completely omits keyboard accessibility and screen reader labels. Additionally, dynamic updates like toast feedback and header badge counter changes go unnoticed by assistive tech unless explicitly configured with `role="status"` and `aria-live="polite"`.
**Action:** Always replace icon-only clickable `<span>` elements with semantic `<button type="button">` featuring attribute-escaped ARIA labels (`aria-label`), provide button reset CSS to preserve visual design, and establish live regions (`aria-live="polite"`) for status announcements and cart quantity indicators.
