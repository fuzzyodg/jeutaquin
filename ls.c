#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <pwd.h>
#include <grp.h>
#include <time.h>
#include <errno.h>

// Structure pour stocker les options passees en parametre
typedef struct {
    int opt_a; // afficher fichiers caches
    int opt_F; // afficher indicateurs (/, *, etc.)
    int opt_r; // tri inverse
    int opt_l; // format long
} Options;

// Structure pour stocker les infos d'un fichier du dossier
typedef struct {
    char name[256];
    char fullpath[1024];
    struct stat st;
    int has_stat;
} Fichier;

// Comparaison pour le tri alphabetique
int compare_asc(const void *a, const void *b) {
    Fichier *f1 = (Fichier *)a;
    Fichier *f2 = (Fichier *)b;
    return strcmp(f1->name, f2->name);
}

int compare_desc(const void *a, const void *b) {
    Fichier *f1 = (Fichier *)a;
    Fichier *f2 = (Fichier *)b;
    return strcmp(f2->name, f1->name);
}

// Affichage des permissions au format drwxr-xr-x
void afficher_droits(mode_t mode) {
    char droits[11];

    if (S_ISDIR(mode)) droits[0] = 'd';
    else if (S_ISLNK(mode)) droits[0] = 'l';
    else if (S_ISCHR(mode)) droits[0] = 'c';
    else if (S_ISBLK(mode)) droits[0] = 'b';
    else if (S_ISFIFO(mode)) droits[0] = 'p';
    else if (S_ISSOCK(mode)) droits[0] = 's';
    else droits[0] = '-';

    droits[1] = (mode & S_IRUSR) ? 'r' : '-';
    droits[2] = (mode & S_IWUSR) ? 'w' : '-';
    droits[3] = (mode & S_IXUSR) ? 'x' : '-';

    droits[4] = (mode & S_IRGRP) ? 'r' : '-';
    droits[5] = (mode & S_IWGRP) ? 'w' : '-';
    droits[6] = (mode & S_IXGRP) ? 'x' : '-';

    droits[7] = (mode & S_IROTH) ? 'r' : '-';
    droits[8] = (mode & S_IWOTH) ? 'w' : '-';
    droits[9] = (mode & S_IXOTH) ? 'x' : '-';

    droits[10] = '\0';
    printf("%s", droits);
}

// Caractere special pour l'option -F
char ObtenirIndicateur(mode_t mode) {
    if (S_ISDIR(mode)) return '/';
    if (S_ISLNK(mode)) return '@';
    if (S_ISFIFO(mode)) return '|';
    if (S_ISSOCK(mode)) return '=';
    if (mode & (S_IXUSR | S_IXGRP | S_IXOTH)) return '*';
    return '\0';
}

void afficher_fichier(Fichier *f, Options *opts) {
    char ind = '\0';
    if (opts->opt_F && f->has_stat) {
        ind = ObtenirIndicateur(f->st.st_mode);
    }

    if (opts->opt_l) {
        if (f->has_stat) {
            afficher_droits(f->st.st_mode);
            printf(" %2lu", (unsigned long)f->st.st_nlink);

            struct passwd *pw = getpwuid(f->st.st_uid);
            struct group  *gr = getgrgid(f->st.st_gid);

            if (pw) printf(" %-8s", pw->pw_name);
            else printf(" %-8u", f->st.st_uid);

            if (gr) printf(" %-8s", gr->gr_name);
            else printf(" %-8u", f->st.st_gid);

            printf(" %8lu", (unsigned long)f->st.st_size);

            char datebuf[64];
            struct tm *t = localtime(&f->st.st_mtime);
            if (t) {
                strftime(datebuf, sizeof(datebuf), "%b %e %H:%M", t);
                printf(" %s", datebuf);
            } else {
                printf(" %12s", "???");
            }

            if (ind != '\0') printf(" %s%c\n", f->name, ind);
            else printf(" %s\n", f->name);
        } else {
            printf("?????????? ? ? ? ? ? %s\n", f->name);
        }
    } else {
        if (ind != '\0') printf("%s%c  ", f->name, ind);
        else printf("%s  ", f->name);
    }
}

void lister_dossier(const char *path, Options *opts, int plusieurs) {
    DIR *d = opendir(path);
    if (!d) {
        fprintf(stderr, "mon_ls: impossible d'accéder à '%s': %s\n", path, strerror(errno));
        return;
    }

    if (plusieurs) {
        printf("%s:\n", path);
    }

    int cap = 32;
    int total = 0;
    Fichier *liste = malloc(cap * sizeof(Fichier));
    if (!liste) {
        perror("malloc");
        closedir(d);
        return;
    }

    struct dirent *ent;
    while ((ent = readdir(d)) != NULL) {
        // Ignorer fichiers cachés si pas -a
        if (!opts->opt_a && ent->d_name[0] == '.') {
            continue;
        }

        if (total >= cap) {
            cap *= 2;
            Fichier *tmp = realloc(liste, cap * sizeof(Fichier));
            if (!tmp) break;
            liste = tmp;
        }

        strncpy(liste[total].name, ent->d_name, 255);
        liste[total].name[255] = '\0';

        if (strcmp(path, "/") == 0) {
            snprintf(liste[total].fullpath, sizeof(liste[total].fullpath), "/%s", ent->d_name);
        } else {
            snprintf(liste[total].fullpath, sizeof(liste[total].fullpath), "%s/%s", path, ent->d_name);
        }

        if (lstat(liste[total].fullpath, &liste[total].st) == 0) {
            liste[total].has_stat = 1;
        } else {
            liste[total].has_stat = 0;
        }

        total++;
    }
    closedir(d);

    // Tri
    if (opts->opt_r) {
        qsort(liste, total, sizeof(Fichier), compare_desc);
    } else {
        qsort(liste, total, sizeof(Fichier), compare_asc);
    }

    for (int i = 0; i < total; i++) {
        afficher_fichier(&liste[i], opts);
    }

    if (!opts->opt_l && total > 0) {
        printf("\n");
    }

    free(liste);
}

int main(int argc, char *argv[]) {
    Options opts = {0, 0, 0, 0};
    char *dossiers[256];
    int nb_dossiers = 0;

    // Analyse des arguments
    for (int i = 1; i < argc; i++) {
        if (argv[i][0] == '-' && argv[i][1] != '\0') {
            for (int j = 1; argv[i][j] != '\0'; j++) {
                if (argv[i][j] == 'a') opts.opt_a = 1;
                else if (argv[i][j] == 'F') opts.opt_F = 1;
                else if (argv[i][j] == 'r') opts.opt_r = 1;
                else if (argv[i][j] == 'l') opts.opt_l = 1;
                else {
                    fprintf(stderr, "mon_ls: option invalide -- '%c'\n", argv[i][j]);
                    fprintf(stderr, "Utilisation: mon_ls [-a] [-F] [-r] [-l] [répertoire...]\n");
                    return 1;
                }
            }
        } else {
            dossiers[nb_dossiers++] = argv[i];
        }
    }

    if (nb_dossiers == 0) {
        dossiers[0] = ".";
        nb_dossiers = 1;
    }

    for (int i = 0; i < nb_dossiers; i++) {
        if (i > 0) printf("\n");
        lister_dossier(dossiers[i], &opts, nb_dossiers > 1);
    }

    return 0;
}
