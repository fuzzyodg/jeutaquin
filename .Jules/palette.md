## 2026-05-18 - Shopping Cart Icon-Only Buttons Accessibility

**Learning:** In dynamically rendered shopping cart items, icon-only controls (like `−`, `+`, `🗑`, and `✕` close buttons) lack accessible labels unless explicitly provided with `aria-label` attributes. Using a non-interactive `<span>` for item removal prevents keyboard users from focusing and removing items via Tab/Space/Enter navigation. Escaping attribute content with `escAttr()` ensures safe HTML attribute injection for item names with quotes or special characters.

**Action:** Always render cart removal controls as semantic `<button>` elements with descriptive `aria-label` strings (e.g. `aria-label="Supprimer ${escAttr(item.name)} du panier"`), and ensure all close / quantity icon buttons have clear localized ARIA labels.
