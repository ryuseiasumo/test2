#include <stdio.h>
#include <string.h>

char *str_cpy(char *d,const char *s)
{
	char *t = d;
	while (*d++ = *s++);
	return t;
}

int main(int argc, char const *argv[])
{
	char str[128] = "ABC";
	char *p = "DEF";
	char str_2[128] = "GHI";

	p = str;
	printf("%s\n", p);

	str_cpy(str,str_2);
	printf("%s\n", str);

	str_cpy(str_2,p);
	printf("%s\n", str_2);

	strcpy(str,str_2);
	printf("%s\n", str);




	return 0;
}