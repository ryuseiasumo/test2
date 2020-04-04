#include <stdio.h>


int str_length(const char *s)
{
	int len = 0;

	//null文字になったら終了
	while (*s++)
		len++;
	return len;
}

int main(void)
{
	char str[128];

	printf("文字列を入力して下さい：");   scanf("%s", str);

	printf("%sの長さは%dです\n", str, str_length(str));
	printf("%sのアドレスは%pです\n", str, str);

	return 0;
}