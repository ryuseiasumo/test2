#include <stdio.h>
#include <stdlib.h>

int islake=0;
int count=0;
int N=10;
int M=12;
char field[10][13]={{'W', '.', '.',  '.', '.', '.', '.', '.', '.', 'W', 'W', '.'},
         {'.', 'W', 'W', 'W', '.', '.', '.', '.', '.', 'W', 'W', 'W'},
         {'.', '.', '.', '.', 'W', 'W', '.', '.', '.', 'W', 'W', '.'},
         {'.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', '.'},
         {'.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', '.', '.'},
         {'.', '.', 'W', '.', '.', '.', '.', '.', '.', 'W', '.', '.'},
         {'.', 'W', '.', 'W', '.', '.', '.', '.', '.', 'W', 'W', '.'},
         {'W', '.', 'W', '.', 'W', '.', '.', '.', '.', '.', 'W', '.'},
         {'.', 'W', '.', 'W', '.', '.', '.', '.', '.', '.', 'W', '.'},
         {'.', '.', 'W', '.', '.', '.', '.', '.', '.', '.', 'W', '.'}};

bool lake(int tate,int yoko){
    printf("%d",tate);
    printf("%d\n",yoko);
    if(tate<0 || yoko<0 || tate>N || yoko>13){
        return true;
    }

    if(field[tate][yoko]=='.'){
        return true;
    }

    else if(field[tate][yoko]=='W'){
        printf("%s","a");
        islake=1;
        field[tate][yoko]='.';
        lake(tate,yoko+1);
        lake(tate,yoko-1);
        lake(tate-1,yoko);
        lake(tate+1,yoko);
        lake(tate+1,yoko+1);
        lake(tate-1,yoko-1);
        lake(tate+1,yoko-1);
        lake(tate-1,yoko+1);
    }
    return true;
}

void solve(){
    for(int i=0;i<N;i++){
        for(int u=0;u<M;u++){
            lake(i,u);
            if (islake==1){
                printf("%s","count");
                count++;
                islake=0;
            }
        }
    }
}


int main(){
    solve();
    printf("%d",count);
}
