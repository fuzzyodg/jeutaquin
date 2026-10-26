#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <limits.h>
#include <errno.h>

int main(int argc, char *argv[]) {
    const char *dossier_cible = NULL;

    if (argc > 2) {
        fprintf(stderr, "mon_cd: trop d'arguments\n");
        fprintf(stderr, "Utilisation: mon_cd [répertoire]\n");
        return 1;
    }

    // Gestion du dossier destination
    if (argc == 1 || (argc == 2 && strcmp(argv[1], "~") == 0)) {
        dossier_cible = getenv("HOME");
        if (!dossier_cible) {
            fprintf(stderr, "mon_cd: variable HOME non définie\n");
            return 1;
        }
    } else if (argc == 2 && strcmp(argv[1], "-") == 0) {
        dossier_cible = getenv("OLDPWD");
        if (!dossier_cible) {
            fprintf(stderr, "mon_cd: variable OLDPWD non définie\n");
            return 1;
        }
    } else {
        dossier_cible = argv[1];
    }

    // Changement de repertoire
    if (chdir(dossier_cible) != 0) {
        fprintf(stderr, "mon_cd: impossible d'accéder à '%s': %s\n", dossier_cible, strerror(errno));
        return 1;
    }

    // On recupere le nouveau chemin courant
    char rep_courant[PATH_MAX];
    if (getcwd(rep_courant, sizeof(rep_courant)) != NULL) {
        printf("%s\n", rep_courant);
    } else {
        perror("getcwd");
        return 1;
    }

    return 0;
}
