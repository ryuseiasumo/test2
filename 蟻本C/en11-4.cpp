#include <stdio.h>

void put_string(const char *s)
{
	printf("%s\n", s);
	printf("%p\n", s);
}

int main(void)
{
	char a[4] = "ABC";

	put_string(a);

	return 0;
}