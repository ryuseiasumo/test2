#include <stdio.h>


char *str_copy(char *d, const char *s)
{
	char *t = d;

	while (*d++ = *s++)
		;

	return t;
}


int main(void)
{
	char str[128] = "ABC";
	char tmp[128];

	printf("コピーする文字列");     scanf("%s", tmp);
	printf("%s\n", str_copy(str,tmp));

	return 0;
}