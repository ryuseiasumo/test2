#include <stdio.h>
#include <string.h>

size_t strlen(const char *s)
{
	size_t len = 0;

	while (*s++)
	{
		len++;
	}

	return len;
}

int main(int argc, char const *argv[])
{
	printf("文字列を入力してください");

	return 0;
}