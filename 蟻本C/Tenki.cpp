#include <stdio.h>

char S[4],T[4];

int main(int argc, char const *argv[])
{
	int corrct = 0;
	scanf("%s", S);
	scanf("%s", T);

	for (int i = 0; i < 3; ++i)
	{
		if (S[i] == T[i])
		{
			corrct++;
		}
	}

	printf("%d\n", corrct);

	return 0;
}