#include <stdio.h>
#include <stdlib.h>
int lignevide;
int colonnevide;
void initialisation(int grille[3][3]){
    int num =1;
    for (int i=0 ;i <3 ;i++){
        for(int j =0 ;j<3 ;j++){
            if ( i==2 && j==2){
                grille[i][j]=0;
                lignevide=i;
                colonnevide=j;
            }
            else{
                grille[i][j]=num++;
            }
                
            }
        }
    }
int deplacer(int grille[3][3],char direction);
void melanger(int grille [3][3]){
    char direction[]={'a','b','c','d'};
    for (int k =0; k<1000; k++){
        int alea=rand()%4;
        char dir=direction[alea];
        deplacer(grille,dir);
    }
}
    void afficher(int grille[3][3]){
        for (int i=0 ;i <3 ;i++){
          for(int j =0 ;j<3 ;j++){
            if (grille[i][j]=0){
                printf("   |");
            }
            else{
                printf("%2d |",grille[i][j]);
            }
        }   printf ("\n");
        }
        printf("\n");

    }
int deplacer (int grille[3][3], char direction){
    int nouvligne=lignevide;
    int nouvcolonne=colonnevide;
    switch (direction){
     case 'a':
        nouvligne--;
        break;
     case 'b':
        nouvligne++;
        break;
     case 'c':
        nouvcolonne--;
        break;
     case 'd':
        nouvcolonne++;
        break;
     
     default:
        return 0;
     }
    if (nouvligne>=0 && nouvligne<3 && nouvcolonne>= 0 && nouvcolonne< 3){
        grille[lignevide][colonnevide]=grille[nouvligne][nouvcolonne];
        // 2. La case voisine devient 0 (vide)
        grille[nouvligne][nouvcolonne] = 0;
        lignevide=nouvligne;
        colonnevide=lignevide;
        return 1;
    }
    else
    return 0;
}    
    
int main (){
    int grille[3][3], direction ;
    initialisation(grille);
    melanger(grille);
    afficher(grille);
    deplacer(grille,direction);
    return 0;
}