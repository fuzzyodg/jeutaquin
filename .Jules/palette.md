## 2025-05-15 - Accessibilité des Sliders
**Learning:** L'utilisation de `<span>` pour les indicateurs de pagination (dots) des sliders empêche la navigation au clavier et ne fournit aucun contexte aux lecteurs d'écran. Convertir ces éléments en `<button>` avec des `aria-label` descriptifs est essentiel pour la conformité WCAG sans altérer le design visuel.
**Action:** Toujours utiliser des éléments `<button>` pour les contrôles interactifs et s'assurer que les styles `:focus-visible` sont définis pour garantir une expérience de navigation au clavier fluide.
