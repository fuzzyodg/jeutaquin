#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <limits.h>
#include <errno.h>

int main(int argc, char *argv[]) {
    const char *target_dir = NULL;

    if (argc > 2) {
        fprintf(stderr, "mon_cd: trop d'arguments\n");
        fprintf(stderr, "Utilisation: mon_cd [répertoire]\n");
        return EXIT_FAILURE;
    }

    if (argc == 1) {
        target_dir = getenv("HOME");
        if (!target_dir) {
            fprintf(stderr, "mon_cd: variable HOME non définie\n");
            return EXIT_FAILURE;
        }
    } else {
        target_dir = argv[1];
    }

    if (chdir(target_dir) != 0) {
        fprintf(stderr, "mon_cd: impossible d'accéder à '%s': %s\n", target_dir, strerror(errno));
        return EXIT_FAILURE;
    }

    char cwd[PATH_MAX];
    if (getcwd(cwd, sizeof(cwd)) != NULL) {
        printf("Répertoire actuel : %s\n", cwd);
    } else {
        perror("getcwd");
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
