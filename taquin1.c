#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// --- 1. CONFIGURATION GLOBALE ---
#define TAILLE 4 

// Variables globales pour savoir où est la case vide sans pointeurs
int ligneVide = 3;
int colonneVide = 3;

// --- 2. PROTOTYPES (Déclarations) ---
void initialiserJeu(int grille[TAILLE][TAILLE]);
void melangerGrille(int grille[TAILLE][TAILLE]);
void afficherGrille(int grille[TAILLE][TAILLE]);
int deplacerCase(int grille[TAILLE][TAILLE], char direction);
int verifierVictoire(int grille[TAILLE][TAILLE]);
void viderBuffer();

// --- 3. FONCTION PRINCIPALE (LE MOTEUR) ---
int main() {
    // A. Déclaration de la grille (Le plateau de jeu)
    // On crée un tableau de 4 lignes sur 4 colonnes.
    int grille[TAILLE][TAILLE];

    // B. Initialisation du hasard
    // L'ordinateur a besoin d'une "graine" basée sur l'heure pour que le mélange
    // soit différent à chaque fois que tu lances le jeu.
    srand(time(NULL));

    // C. Création et Mélange
    initialiserJeu(grille);    // On remplit la grille avec 1, 2, 3... et 0.
    melangerGrille(grille);    // On la brouille.

    // D. Variables de boucle
    char choix;      // Stockera la touche pressée par le joueur (Z, S, Q, D)
    int gagne = 0;   // Drapeau : 0 = partie en cours, 1 = victoire.

    // E. La Boucle de Jeu (Le cœur du programme)
    // Tant que 'gagne' vaut 0, on répète tout ce qui est entre accolades.
    while (gagne == 0) {
        
        // 1. Effacer l'écran (Nettoyage)
        // "cls" est pour Windows, "clear" pour Linux/Mac. Le "||" essaie l'un ou l'autre.
        system("cls || clear"); 
        
        // 2. Affichage de l'interface
        printf("=== JEU DE TAQUIN ===\n\n");
        afficherGrille(grille); // On appelle la fonction dédiée à l'affichage.
        
        // 3. Demande au joueur
        printf("\nUtilisez Z (Haut), S (Bas), Q (Gauche), D (Droite) ou 0 pour quitter.\n");
        printf("Votre choix : ");
        
        // 4. Récupération de la touche
        // Le " %c" (avec un espace) est important pour ignorer la touche "Entrée" précédente.
        scanf(" %c", &choix); 
        viderBuffer(); // On nettoie la mémoire du clavier pour éviter les bugs.

        // 5. Gestion de la touche "Quitter"
        if (choix == '0') {
            printf("Au revoir !\n");
            return 0; // Arrête immédiatement le programme (fermeture).
        }

        // 6. Tentative de déplacement
        // On envoie la grille et la touche choisie à la fonction de déplacement.
        deplacerCase(grille, choix);

        // 7. Vérification de la victoire
        // Est-ce que la grille est dans l'ordre (1, 2, 3...) ?
        if (verifierVictoire(grille)) {
            gagne = 1; // Si oui, on change la variable pour arrêter la boucle.
        }
    }

    // F. Écran de fin
    system("cls || clear");
    printf("=== JEU DE TAQUIN ===\n\n");
    afficherGrille(grille);
    printf("\n\nBRAVO ! Vous avez reconstitue la grille !\n");

    return 0; // Fin normale du programme.
}

// --- 4. DÉFINITION DES FONCTIONS ---

// FONCTION 1 : Initialisation
// But : Remplir la grille avec les chiffres dans l'ordre (1 à 15) et mettre 0 en bas à droite.
void initialiserJeu(int grille[TAILLE][TAILLE]) {
    int compteur = 1;
    // Double boucle pour visiter chaque case
    for (int i = 0; i < TAILLE; i++) {
        for (int j = 0; j < TAILLE; j++) {
            grille[i][j] = compteur;
            compteur++;
        }
    }
    // On force la dernière case à 0 (vide)
    grille[TAILLE - 1][TAILLE - 1] = 0;
    
    // On mémorise sa position globalement
    ligneVide = TAILLE - 1;
    colonneVide = TAILLE - 1;
}

// FONCTION 2 : Mélange
// But : Faire 1000 mouvements aléatoires pour mélanger les cases.
void melangerGrille(int grille[TAILLE][TAILLE]) {
    char directions[] = {'z', 's', 'q', 'd'};
    
    // On boucle 1000 fois
    for (int k = 0; k < 1000; k++) {
        // On choisit un chiffre entre 0 et 3 au hasard
        int aleatoire = rand() % 4; 
        // On prend la lettre correspondante (z, s, q ou d)
        char dir = directions[aleatoire];
        // On execute le déplacement (comme si le joueur jouait très vite)
        deplacerCase(grille, dir);
    }
}

// FONCTION 3 : Affichage
// But : Dessiner la grille et les bordures dans la console.
void afficherGrille(int grille[TAILLE][TAILLE]) {
    for (int i = 0; i < TAILLE; i++) {
        printf("---------------------\n"); // Ligne horizontale de séparation
        printf("|"); 
        for (int j = 0; j < TAILLE; j++) {
            if (grille[i][j] == 0) {
                printf("   |"); // Si c'est 0, on affiche du vide (espaces)
            } else {
                printf(" %2d|", grille[i][j]); // Sinon on affiche le nombre
            }
        }
        printf("\n"); // Saut de ligne à la fin de chaque rangée
    }
    printf("---------------------\n"); // Dernière ligne du bas
}

// FONCTION 4 : Déplacement
// But : Calculer le nouveau mouvement, vérifier si c'est valide, et échanger les cases.
int deplacerCase(int grille[TAILLE][TAILLE], char direction) {
    // On commence par supposer qu'on va rester sur place
    int nouvelleLigne = ligneVide;
    int nouvelleColonne = colonneVide;

    // On ajuste les coordonnées selon la touche pressée
    switch (direction) {
        case 'z': nouvelleLigne--; break;    // Monter (ligne - 1)
        case 's': nouvelleLigne++; break;    // Descendre (ligne + 1)
        case 'q': nouvelleColonne--; break;  // Gauche (colonne - 1)
        case 'd': nouvelleColonne++; break;  // Droite (colonne + 1)
        default: return 0; // Si ce n'est pas une touche connue, on arrête.
    }

    // Vérification des limites (Est-ce qu'on sort de la grille ?)
    // Les indices valides vont de 0 à TAILLE-1 (donc 0 à 3).
    if (nouvelleLigne >= 0 && nouvelleLigne < TAILLE && 
        nouvelleColonne >= 0 && nouvelleColonne < TAILLE) {
        
        // ÉCHANGE DES VALEURS :
        // 1. La case vide prend la valeur de la case voisine
        grille[ligneVide][colonneVide] = grille[nouvelleLigne][nouvelleColonne];
        // 2. La case voisine devient 0 (vide)
        grille[nouvelleLigne][nouvelleColonne] = 0;

        // Mise à jour de la position du vide pour le prochain tour
        ligneVide = nouvelleLigne;
        colonneVide = nouvelleColonne;
        
        return 1; // On dit que ça a marché
    } else {
        return 0; // On a touché un mur, mouvement impossible
    }
}

// FONCTION 5 : Vérification de Victoire
// But : Parcourir toute la grille pour voir si les chiffres sont bien rangés 1..15
int verifierVictoire(int grille[TAILLE][TAILLE]) {
    int compteur = 1;
    for (int i = 0; i < TAILLE; i++) {
        for (int j = 0; j < TAILLE; j++) {
            
            // Cas spécial : La toute dernière case (en bas à droite)
            if (i == TAILLE - 1 && j == TAILLE - 1) {
                if (grille[i][j] != 0) return 0; // Elle doit contenir 0
            } 
            // Cas normal : Toutes les autres cases
            else {
                if (grille[i][j] != compteur) return 0; // Si ce n'est pas le bon chiffre -> Perdu
                compteur++; // On passe au chiffre suivant pour la prochaine vérif
            }
        }
    }
    return 1; // Si on a fini la boucle sans erreur, c'est gagné !
}

// FONCTION 6 : Utilitaire (Nettoyage)
// But : Vider le "Buffer" (la mémoire tampon) du clavier.
void viderBuffer() {
    int c;
    // On lit les caractères un par un jusqu'à trouver le "Entrée" (\n)
    while ((c = getchar()) != '\n' && c != EOF);
}