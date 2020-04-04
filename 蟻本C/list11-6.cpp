#include <stdio.h>

char *copy(char *a,const char *b)
{
	char *t = a;

	while (*a++ = *b++)
	{
		;
	}

	return t;
}


int main(int argc, char const *argv[])
{
	char a[128] = "ABC";
	char b[128];

	printf("元の文字列a:%s\n", a);
	printf("コピーしたい文字列b：");   scanf("%s", b);
	copy(a, b);

	printf("文字列a:%s\n", a);
	printf("文字列b:%s\n", b);
	
	return 0;
}