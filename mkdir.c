#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <errno.h>

typedef struct {
    int create_parents; /* -p */
} Options;

static int make_path(const char *path, mode_t mode) {
    char *copypath = strdup(path);
    if (!copypath) {
        perror("strdup");
        return -1;
    }

    size_t len = strlen(copypath);
    if (len > 0 && copypath[len - 1] == '/') {
        copypath[len - 1] = '\0';
    }

    char *p = copypath;
    if (*p == '/') {
        p++;
    }

    while (*p != '\0') {
        if (*p == '/') {
            *p = '\0';
            if (mkdir(copypath, mode) != 0) {
                if (errno != EEXIST) {
                    fprintf(stderr, "mon_mkdir: impossible de créer le répertoire '%s': %s\n", copypath, strerror(errno));
                    free(copypath);
                    return -1;
                }
            }
            *p = '/';
        }
        p++;
    }

    if (mkdir(copypath, mode) != 0) {
        if (errno != EEXIST) {
            fprintf(stderr, "mon_mkdir: impossible de créer le répertoire '%s': %s\n", copypath, strerror(errno));
            free(copypath);
            return -1;
        }
    }

    free(copypath);
    return 0;
}

static int create_directory(const char *path, const Options *opts) {
    mode_t mode = 0755;

    if (opts->create_parents) {
        return make_path(path, mode);
    } else {
        if (mkdir(path, mode) != 0) {
            fprintf(stderr, "mon_mkdir: impossible de créer le répertoire '%s': %s\n", path, strerror(errno));
            return -1;
        }
    }
    return 0;
}

int main(int argc, char *argv[]) {
    Options opts = {0};
    char *dirs[256];
    int dir_count = 0;

    for (int i = 1; i < argc; i++) {
        if (argv[i][0] == '-' && argv[i][1] != '\0') {
            for (int j = 1; argv[i][j] != '\0'; j++) {
                switch (argv[i][j]) {
                    case 'p':
                        opts.create_parents = 1;
                        break;
                    default:
                        fprintf(stderr, "mon_mkdir: option invalide -- '%c'\n", argv[i][j]);
                        fprintf(stderr, "Utilisation: mon_mkdir [-p] <répertoire1> [répertoire2 ...]\n");
                        return EXIT_FAILURE;
                }
            }
        } else {
            dirs[dir_count++] = argv[i];
        }
    }

    if (dir_count == 0) {
        fprintf(stderr, "mon_mkdir: opérande manquant\n");
        fprintf(stderr, "Utilisation: mon_mkdir [-p] <répertoire1> [répertoire2 ...]\n");
        return EXIT_FAILURE;
    }

    int status = EXIT_SUCCESS;
    for (int i = 0; i < dir_count; i++) {
        if (create_directory(dirs[i], &opts) != 0) {
            status = EXIT_FAILURE;
        }
    }

    return status;
}
