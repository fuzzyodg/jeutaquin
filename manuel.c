#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static void print_usage(void) {
    printf("Utilisation : manuel <nom_commande>\n");
    printf("Commandes disponibles : ls, mkdir, cd, manuel\n");
}

static void print_manual_ls(void) {
    printf("NAME\n");
    printf("       ls - affichage du contenu d'un répertoire\n\n");
    printf("SYNOPSIS\n");
    printf("       ls [-a] [-F] [-r] [-l] [répertoire...]\n\n");
    printf("DESCRIPTION\n");
    printf("       Liste les informations sur les fichiers (du répertoire courant par défaut).\n");
    printf("       Les entrées sont triées par ordre alphabétique par défaut.\n\n");
    printf("OPTIONS\n");
    printf("       -a     Ne pas ignorer les entrées commençant par .\n");
    printf("       -F     Ajouter un caractère d'indication (ex: / pour répertoire, * pour exécutable).\n");
    printf("       -r     Inverser l'ordre du tri.\n");
    printf("       -l     Utiliser un format d'affichage long (permissions, propriétaire, groupe, taille, date).\n");
}

static void print_manual_mkdir(void) {
    printf("NAME\n");
    printf("       mkdir - création de répertoires\n\n");
    printf("SYNOPSIS\n");
    printf("       mkdir [-p] <répertoire1> [répertoire2...]\n\n");
    printf("DESCRIPTION\n");
    printf("       Crée le ou les répertoires spécifiés, s'ils n'existent pas déjà.\n\n");
    printf("OPTIONS\n");
    printf("       -p     Crée les répertoires parents si nécessaire, sans erreur si le répertoire existe déjà.\n");
}

static void print_manual_cd(void) {
    printf("NAME\n");
    printf("       cd - changement de répertoire de travail\n\n");
    printf("SYNOPSIS\n");
    printf("       cd [répertoire]\n\n");
    printf("DESCRIPTION\n");
    printf("       Change le répertoire de travail actuel vers le répertoire spécifié.\n");
    printf("       Supporte ~ (dossier personnel) et - (dossier précédent).\n\n");
    printf("OPTIONS\n");
    printf("       Aucune option prise en charge.\n");
}

static void print_manual_manuel(void) {
    printf("NAME\n");
    printf("       manuel - manuel d'utilisation des commandes émulées\n\n");
    printf("SYNOPSIS\n");
    printf("       manuel <nom_commande>\n\n");
    printf("DESCRIPTION\n");
    printf("       Affiche la documentation détaillée d'une commande de l'émulateur.\n");
    printf("       Format structuré Unix standard : NAME, SYNOPSIS, DESCRIPTION, OPTIONS.\n\n");
    printf("OPTIONS\n");
    printf("       Aucune option prise en charge.\n");
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        print_usage();
        return EXIT_FAILURE;
    }

    const char *cmd = argv[1];

    if (strcmp(cmd, "ls") == 0) {
        print_manual_ls();
    } else if (strcmp(cmd, "mkdir") == 0) {
        print_manual_mkdir();
    } else if (strcmp(cmd, "cd") == 0) {
        print_manual_cd();
    } else if (strcmp(cmd, "manuel") == 0) {
        print_manual_manuel();
    } else {
        fprintf(stderr, "manuel: aucune entrée de manuel pour '%s'\n", cmd);
        print_usage();
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
