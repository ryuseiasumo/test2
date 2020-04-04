#include <stdio.h>

int main(void)
{
	int A,B;
	scanf("%d", &A); scanf("%d", &B);
	int C;
	C = A - 2*B;
	if (C <= 0)
		printf("%d\n", 0);

	else
		printf("%d\n", C);

	return 0;

}
