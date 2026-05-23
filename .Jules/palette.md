## 2025-05-15 - [Panier] Accessibilité et UX du panier

**Learning:** Les boutons d'icônes sans texte (fermeture, modification de quantité, suppression) sont invisibles pour les lecteurs d'écran s'ils n'ont pas d'attribut `aria-label`. De plus, un panier vide sans appel à l'action (CTA) constitue une impasse UX qui casse le flux de navigation.

**Action:** Toujours inclure un `aria-label` descriptif sur les boutons d'icônes. Utiliser la délégation d'événements pour gérer les interactions dynamiques de manière plus propre que les attributs `onclick` en ligne. S'assurer que chaque état "vide" (comme un panier vide) redirige l'utilisateur vers une action positive (ex: "Voir le menu").
