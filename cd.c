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
        fprintf(stderr, "cd: trop d'arguments\n");
        fprintf(stderr, "Utilisation: cd [répertoire]\n");
        return EXIT_FAILURE;
    }

    if (argc == 1 || (argc == 2 && strcmp(argv[1], "~") == 0)) {
        target_dir = getenv("HOME");
        if (!target_dir) {
            fprintf(stderr, "cd: variable HOME non définie\n");
            return EXIT_FAILURE;
        }
    } else if (argc == 2 && strcmp(argv[1], "-") == 0) {
        target_dir = getenv("OLDPWD");
        if (!target_dir) {
            fprintf(stderr, "cd: variable OLDPWD non définie\n");
            return EXIT_FAILURE;
        }
    } else {
        target_dir = argv[1];
    }

    char cwd_before[PATH_MAX];
    if (getcwd(cwd_before, sizeof(cwd_before)) == NULL) {
        cwd_before[0] = '\0';
    }

    if (chdir(target_dir) != 0) {
        fprintf(stderr, "cd: impossible d'accéder à '%s': %s\n", target_dir, strerror(errno));
        return EXIT_FAILURE;
    }

    char cwd_after[PATH_MAX];
    if (getcwd(cwd_after, sizeof(cwd_after)) == NULL) {
        perror("getcwd");
        return EXIT_FAILURE;
    }

    /* Print target path on stdout so shell function can execute cd or builtin */
    printf("%s\n", cwd_after);

    return EXIT_SUCCESS;
}
