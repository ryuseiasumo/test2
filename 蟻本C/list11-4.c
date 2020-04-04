#include <stdio.h>


int main(int argc, char const *argv[])
{
	int i;
	char a[][5] = {"LISP", "C", "Ada"};
	char *p[] = {"PAUL", "X", "MAC"};

	int n;

	n = sizeof(a)/(sizeof(a[0]));
	printf("%d\n", n);

	int m = sizeof(p)/(sizeof(p[0]));
	printf("%d\n", m);
	for (int i = 0; i < n; ++i)
	{
		printf("a[%d] = %s\n", i, a[i]);
	}
	for (int i = 0; i < m; ++i)
	{
		printf("p[%d] = %s\n", i, p[i]);
	}
	return 0;
}