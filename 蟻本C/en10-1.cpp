#include <stdio.h>

void adjust_point(int *num)
{
	if (*num < 0)
	{
		*num = 0;
	}

	else if (*num > 100)
	{
		*num = 100;
	}
	 
}


int main(void)
{
	int n;
	printf("n = ");   scanf("%d", &n);

	adjust_point(&n);
	printf("%d\n", n);

	return 0;
}