#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <errno.h>

// Fonction pour repartitionner et creer tous les dossiers parents si -p est actif
int creer_arborescence(const char *path) {
    char chemin_temp[1024];
    strncpy(chemin_temp, path, sizeof(chemin_temp) - 1);
    chemin_temp[sizeof(chemin_temp) - 1] = '\0';

    size_t len = strlen(chemin_temp);
    if (len > 0 && chemin_temp[len - 1] == '/') {
        chemin_temp[len - 1] = '\0';
    }

    char *p = chemin_temp;
    if (*p == '/') p++;

    while (*p != '\0') {
        if (*p == '/') {
            *p = '\0';
            if (mkdir(chemin_temp, 0755) != 0) {
                if (errno != EEXIST) {
                    fprintf(stderr, "mon_mkdir: impossible de créer le répertoire '%s': %s\n", chemin_temp, strerror(errno));
                    return -1;
                }
            }
            *p = '/';
        }
        p++;
    }

    if (mkdir(chemin_temp, 0755) != 0) {
        if (errno != EEXIST) {
            fprintf(stderr, "mon_mkdir: impossible de créer le répertoire '%s': %s\n", chemin_temp, strerror(errno));
            return -1;
        }
    }

    return 0;
}

int main(int argc, char *argv[]) {
    int opt_p = 0;
    char *dossiers[256];
    int nb_dossiers = 0;

    // Analyse des arguments
    for (int i = 1; i < argc; i++) {
        if (argv[i][0] == '-' && argv[i][1] != '\0') {
            for (int j = 1; argv[i][j] != '\0'; j++) {
                if (argv[i][j] == 'p') {
                    opt_p = 1;
                } else {
                    fprintf(stderr, "mon_mkdir: option invalide -- '%c'\n", argv[i][j]);
                    fprintf(stderr, "Utilisation: mon_mkdir [-p] <répertoire1> [répertoire2 ...]\n");
                    return 1;
                }
            }
        } else {
            dossiers[nb_dossiers++] = argv[i];
        }
    }

    if (nb_dossiers == 0) {
        fprintf(stderr, "mon_mkdir: opérande manquant\n");
        fprintf(stderr, "Utilisation: mon_mkdir [-p] <répertoire1> [répertoire2 ...]\n");
        return 1;
    }

    int erreur = 0;
    for (int i = 0; i < nb_dossiers; i++) {
        if (opt_p) {
            if (creer_arborescence(dossiers[i]) != 0) {
                erreur = 1;
            }
        } else {
            if (mkdir(dossiers[i], 0755) != 0) {
                fprintf(stderr, "mon_mkdir: impossible de créer le répertoire '%s': %s\n", dossiers[i], strerror(errno));
                erreur = 1;
            }
        }
    }

    return erreur ? 1 : 0;
}