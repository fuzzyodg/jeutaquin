## 2025-05-15 - Accessibilité et Feedback du Panier d'Achat

**Learning:** L'utilisation d'éléments non sémantiques (`<span>`) avec des gestionnaires d'événements `onclick` en ligne pour les contrôles du panier nuit à l'accessibilité au clavier et à la maintenance du code. De plus, l'absence de retour visuel immédiat lors de l'ajout d'un article (au-delà d'un simple toast) peut laisser l'utilisateur dans l'incertitude quant à la réussite de l'action.

**Action:**
1. Remplacer les `<span>` par des éléments `<button>` sémantiques avec des `aria-label` descriptifs en français.
2. Utiliser la délégation d'événements sur le conteneur du panier pour une gestion plus propre et performante des actions (augmentation, diminution, suppression).
3. Implémenter une animation "bump" (mise à l'échelle temporaire) sur l'icône du panier via CSS et JavaScript pour fournir un retour haptique visuel instantané lors de l'ajout d'articles.
4. Ajouter `aria-live="polite"` aux zones de texte changeant dynamiquement (comme la quantité) pour informer les utilisateurs de lecteurs d'écran.
>>>>>>> REPLACE
