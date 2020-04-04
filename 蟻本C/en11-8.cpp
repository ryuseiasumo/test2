#include <stdio.h>
#include <string.h>
#include <ctype.h>

void del_digit(char *s){

    int i, j;

    for(i = 0; i < strlen(s); i++)
    {
        if(!isalpha(*(s + i)))
        {
            for(j = i; j < strlen(s); j++)
            {
                *(s + j) = *(s + j + 1);
            }
            i--;
        }
    }
}

int main(){

    char str[256];

    printf("文字列を入力してください:");
    scanf("%s", str);

    del_digit(str);
    printf("数字を消しました:%s\n", str);

    return 0;
}