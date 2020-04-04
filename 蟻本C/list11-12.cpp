#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
	char str[4] = "123";
	printf("整数に変換すると%dです\n", atoi(str));
	return 0;
}