#include <stdio.h>

const char *str_chr(const char *s, int c)
{
	while(*s)
	{
		if (*s == c)
		{
			return s;
		}

		s++;
	}

	return NULL;
}


int main(void)
{
	char a[11]= "hataryusei";
	char t = 'r';

	printf("ポインタは、%pです\n", str_chr(a, t));

	return 0;
}

