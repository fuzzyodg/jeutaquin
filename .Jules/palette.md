## 2025-05-24 - Optimisation de la gestion du panier et accessibilité

**Learning:** L'utilisation d'attributs `onclick` directement dans le HTML généré dynamiquement (via JavaScript) crée une dette technique et viole les standards de sécurité/propreté du projet. La délégation d'événements sur un parent stable (`#cart-body`) est la méthode robuste pour gérer les interactions sur des éléments qui entrent et sortent du DOM. De plus, transformer des icônes de suppression (souvent des `<span>` ou `<i>`) en véritables éléments `<button>` est crucial pour que les utilisateurs de lecteurs d'écran puissent interagir avec le panier.

**Action:** Toujours privilégier `addEventListener` sur un conteneur parent pour les listes dynamiques. Remplacer systématiquement les icônes cliquables par des `<button aria-label="...">` pour garantir l'accessibilité clavier et lecteur d'écran.
