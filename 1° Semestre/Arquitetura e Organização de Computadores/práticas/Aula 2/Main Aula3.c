#include <stdio.h>
#include <stdlib.h>


int main(int argc, char *argv[]) 
{
    //int x;
    //for(x=1;x<20;x++)
    //{
      //  printf("\xDB");  
        //sleep(200);
    //}
    //return 0;
    printf("\n Sala \n");
    retangulo (22,13);
    printf("\n Cozinha \n");
    retangulo (16,16);
    printf("\n Banheiro \n");
    retangulo (6,8);
    printf("\n Quarto \n");
    retangulo (12,12);
}

retangulo (largura, altura)
int largura, altura;
{
   int j,k;
   largura /=2;
   altura /=4;
   for(j=1;j<=altura; j++)
       {
         printf("\t \t");
         printf("\n");
           for(k=1;k<=largura;k++)
            {
                printf("\xDB");
            }
        }
}
