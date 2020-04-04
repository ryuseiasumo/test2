#include <stdio.h>
#include <string.h>

int strcmp(const char *s1, const char *s2)
{
	while(*s1 == *s2)
	{
		if (*s1 == '\0')
		{
			return 0;
		}

		else
		{
			s1++;
			s2++;
		}
	}
	return (unsigned char)*s1 - (unsigned char)*s2;
}


int main(int argc, char const *argv[])
{
	char s1[9] = "ABCDZEGH";
	char s2[10] = "ABCDGHjAO";
	printf("%d\n", strcmp(s1 , s2));


	return 0;
}