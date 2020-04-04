#include <stdio.h>
#define MAX_N 100

int N;
char S[MAX_N];
char T[MAX_N];

char ans[MAX_N*2];

int main(int argc, char const *argv[])
{
	scanf("%d", &N);
	scanf("%s", S);
	scanf("%s", T);
	int len = 2*N;

	for (int i = 0; i < N; ++i)
	{
		if (S[i] == '\0')
		{
			break;
		}
		ans[2*i] = S[i];
		ans[2*i+1] = T[i];
	}

	for (int i = 0; i < len; ++i)
	{
		printf("%c", ans[i]);
	}
	printf("\n");

	return 0;
}