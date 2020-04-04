#include <stdio.h>
#include <ctype.h>

void str_toupper(char *s)
{
	while (*s)
	{
		*s = toupper(*s);
		s++;
	}

}

void str_tolower(char *s)
{
	while (*s)
	{
		*s = tolower(*s);
		s++;
	}

}

int main(int argc, char const *argv[])
{
	char str[8] = "ABcdEfG";
	str_toupper(str);
	printf("%s\n", str);
	
	str_tolower(str);
	printf("%s\n", str);

	return 0;
}