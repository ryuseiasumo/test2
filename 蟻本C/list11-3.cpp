#include <stdio.h>

int main(void)
{
	char *p = "123";

	printf("p = \"%s\"\n", p);
	p = "456";

	printf("p = \"%s\"\n", p);

	for (int i = 0; i < 3; ++i)
	{
			printf("p = \"%c\"\n", *(p+i));

	}

	return 0;
}