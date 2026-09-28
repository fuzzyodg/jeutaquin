## 2025-05-20 - Overlay Keyboard Dismissal Pattern
**Learning:** Overlays (shopping cart panels, event modals, and mobile menus) in vanilla JavaScript projects often lack keyboard dismissal, leaving keyboard-only users trapped or forced to manually tab to close buttons.
**Action:** Implement document-level `keydown` listener listening for `Escape` key events that checks active overlay state classes (`.open`, `.active`) and triggers their respective close handlers.
