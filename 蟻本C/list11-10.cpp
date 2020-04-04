#include <stdio.h>
#include <string.h>


char *strcat(char *s1, const char *s2)
{
	char *tmp = s1;

	while (*s1)
	{
		s1++;
	}
	while (*s1++ = *s2++)
	{
		;
	}

	return tmp;
}


// 連結する文字列の長さを制限する
char *strncat(char *s1, const char *s2, size_t n)
{
	char *tmp = s1;
	while (*s1)
	{
		s1++;
	}

	while (n--)
	{
		if (!(*s1++ = *s2++))
		{
			break;
		}
		*s1 = '\0';

	}

	return tmp;

}


int main(void)
{
	char s1[7] = "ABCDEF";
	char s2[6] = "GHIJK";
	strcat(s1, s2);

	printf("%s\n", s1);


	return 0;
}