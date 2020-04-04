#include <stdio.h>

int main(int argc, char const *argv[])
{
	char str[4];
	str[0] = 'A';
	str[1] = 'B';
	str[2] = 'C';
	str[3] = '\0';
	
	printf("%s\n", str);
	return 0;
}