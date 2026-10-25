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

typedef struct {
    int show_all;     /* -a */
    int classify;     /* -F */
    int reverse;      /* -r */
    int long_format;  /* -l */
} Options;

typedef struct {
    char *name;
    char *path;
    struct stat st;
    int has_stat;
} FileEntry;

static int compare_entries_asc(const void *a, const void *b) {
    const FileEntry *e1 = (const FileEntry *)a;
    const FileEntry *e2 = (const FileEntry *)b;
    return strcmp(e1->name, e2->name);
}

static int compare_entries_desc(const void *a, const void *b) {
    const FileEntry *e1 = (const FileEntry *)a;
    const FileEntry *e2 = (const FileEntry *)b;
    return strcmp(e2->name, e1->name);
}

static void print_permissions(mode_t mode) {
    char p[11];
    p[0] = S_ISDIR(mode)  ? 'd' :
           S_ISLNK(mode)  ? 'l' :
           S_ISCHR(mode)  ? 'c' :
           S_ISBLK(mode)  ? 'b' :
           S_ISFIFO(mode) ? 'p' :
           S_ISSOCK(mode) ? 's' : '-';

    p[1] = (mode & S_IRUSR) ? 'r' : '-';
    p[2] = (mode & S_IWUSR) ? 'w' : '-';
    p[3] = (mode & S_IXUSR) ? 'x' : '-';

    p[4] = (mode & S_IRGRP) ? 'r' : '-';
    p[5] = (mode & S_IWGRP) ? 'w' : '-';
    p[6] = (mode & S_IXGRP) ? 'x' : '-';

    p[7] = (mode & S_IROTH) ? 'r' : '-';
    p[8] = (mode & S_IWOTH) ? 'w' : '-';
    p[9] = (mode & S_IXOTH) ? 'x' : '-';

    p[10] = '\0';
    printf("%s", p);
}

static char get_file_indicator(mode_t mode) {
    if (S_ISDIR(mode)) return '/';
    if (S_ISLNK(mode)) return '@';
    if (S_ISFIFO(mode)) return '|';
    if (S_ISSOCK(mode)) return '=';
    if (mode & (S_IXUSR | S_IXGRP | S_IXOTH)) return '*';
    return '\0';
}

static void print_entry(const FileEntry *entry, const Options *opts) {
    char indicator = '\0';
    if (opts->classify && entry->has_stat) {
        indicator = get_file_indicator(entry->st.st_mode);
    }

    if (opts->long_format) {
        if (entry->has_stat) {
            print_permissions(entry->st.st_mode);
            printf(" %2lu", (unsigned long)entry->st.st_nlink);

            struct passwd *pw = getpwuid(entry->st.st_uid);
            struct group  *gr = getgrgid(entry->st.st_gid);

            if (pw) {
                printf(" %-8s", pw->pw_name);
            } else {
                printf(" %-8u", entry->st.st_uid);
            }

            if (gr) {
                printf(" %-8s", gr->gr_name);
            } else {
                printf(" %-8u", entry->st.st_gid);
            }

            printf(" %8lu", (unsigned long)entry->st.st_size);

            char date_str[64];
            struct tm *tm_info = localtime(&entry->st.st_mtime);
            if (tm_info) {
                strftime(date_str, sizeof(date_str), "%b %e %H:%M", tm_info);
                printf(" %s", date_str);
            } else {
                printf(" %12s", "???");
            }

            if (indicator != '\0') {
                printf(" %s%c\n", entry->name, indicator);
            } else {
                printf(" %s\n", entry->name);
            }
        } else {
            /* Fallback if stat failed */
            printf("?????????? ? ?        ?        ?            ? %s\n", entry->name);
        }
    } else {
        if (indicator != '\0') {
            printf("%s%c  ", entry->name, indicator);
        } else {
            printf("%s  ", entry->name);
        }
    }
}

static void list_directory(const char *dirpath, const Options *opts, int print_dirname) {
    DIR *dir = opendir(dirpath);
    if (!dir) {
        fprintf(stderr, "mon_ls: impossible d'accéder à '%s': %s\n", dirpath, strerror(errno));
        return;
    }

    if (print_dirname) {
        printf("%s:\n", dirpath);
    }

    size_t capacity = 16;
    size_t count = 0;
    FileEntry *entries = malloc(capacity * sizeof(FileEntry));
    if (!entries) {
        perror("malloc");
        closedir(dir);
        return;
    }

    struct dirent *dp;
    while ((dp = readdir(dir)) != NULL) {
        if (!opts->show_all && dp->d_name[0] == '.') {
            continue;
        }

        if (count >= capacity) {
            capacity *= 2;
            FileEntry *new_entries = realloc(entries, capacity * sizeof(FileEntry));
            if (!new_entries) {
                perror("realloc");
                break;
            }
            entries = new_entries;
        }

        entries[count].name = strdup(dp->d_name);

        size_t full_path_len = strlen(dirpath) + strlen(dp->d_name) + 2;
        entries[count].path = malloc(full_path_len);
        if (entries[count].path) {
            if (strcmp(dirpath, "/") == 0) {
                snprintf(entries[count].path, full_path_len, "/%s", dp->d_name);
            } else {
                snprintf(entries[count].path, full_path_len, "%s/%s", dirpath, dp->d_name);
            }
        }

        if (lstat(entries[count].path, &entries[count].st) == 0) {
            entries[count].has_stat = 1;
        } else {
            entries[count].has_stat = 0;
        }

        count++;
    }
    closedir(dir);

    /* Sort entries */
    if (opts->reverse) {
        qsort(entries, count, sizeof(FileEntry), compare_entries_desc);
    } else {
        qsort(entries, count, sizeof(FileEntry), compare_entries_asc);
    }

    /* Long format total block count calculation could be done if needed, but not required */

    /* Print entries */
    for (size_t i = 0; i < count; i++) {
        print_entry(&entries[i], opts);
    }

    if (!opts->long_format && count > 0) {
        printf("\n");
    }

    /* Cleanup */
    for (size_t i = 0; i < count; i++) {
        free(entries[i].name);
        free(entries[i].path);
    }
    free(entries);
}

int main(int argc, char *argv[]) {
    Options opts = {0, 0, 0, 0};
    char *dirs[256];
    int dir_count = 0;

    for (int i = 1; i < argc; i++) {
        if (argv[i][0] == '-' && argv[i][1] != '\0') {
            for (int j = 1; argv[i][j] != '\0'; j++) {
                switch (argv[i][j]) {
                    case 'a':
                        opts.show_all = 1;
                        break;
                    case 'F':
                        opts.classify = 1;
                        break;
                    case 'r':
                        opts.reverse = 1;
                        break;
                    case 'l':
                        opts.long_format = 1;
                        break;
                    default:
                        fprintf(stderr, "mon_ls: option invalide -- '%c'\n", argv[i][j]);
                        fprintf(stderr, "Utilisation: mon_ls [-a] [-F] [-r] [-l] [répertoire...]\n");
                        return EXIT_FAILURE;
                }
            }
        } else {
            dirs[dir_count++] = argv[i];
        }
    }

    if (dir_count == 0) {
        dirs[0] = ".";
        dir_count = 1;
    }

    for (int i = 0; i < dir_count; i++) {
        if (i > 0) {
            printf("\n");
        }
        list_directory(dirs[i], &opts, dir_count > 1);
    }

    return EXIT_SUCCESS;
}
