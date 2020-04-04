#include <stdio.h>

int str_chnum(const char *s, int c)
{
	int ans = 0;
	while(*s)
	{
		if (*s == c)
		{
			ans++;
		}

		s++;
	}

	return ans;
}



int main(int argc, char const *argv[])
{
	char a[11]= "hataryusei";
	char t = 'h';

	printf("回数は、%d回です\n", str_chnum(a, t));

	return 0;
}

