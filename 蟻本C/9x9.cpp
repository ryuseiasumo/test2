#include <stdio.h>

int main(int argc, char const *argv[])
{
	int A, B;
	scanf("%d", &A);
	scanf("%d", &B);

	if (A <= 9 && B <= 9)
	{
		printf("%d\n", A*B);
	}

	else
	{
		printf("%d", -1);
	}


	return 0;
}