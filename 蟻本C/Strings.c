#include <stdio.h>
#define MAX 100

char S[MAX];
char T[MAX];
char ans[MAX*2];

int main(void){
	scanf("%s", S);
	scanf("%s", T);	

	int i = 0, j = 0;
	int length = 0;

	while(T[i] != '\0' ){
		ans[i] = T[i];
		length++;
		i++;
	}

	while(S[j] != '\0'){
		ans[length+j] = S[j];
		j++;
	}

	printf("%s\n", ans);


	return 0;
}