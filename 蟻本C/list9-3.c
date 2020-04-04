#include <stdio.h>

int main(int argc, char const *argv[])
{
	char str[48];

	printf("お名前は？\n");
	scanf("%s", str);
	printf("こんにちは%sさん\n", str);

	char *name;
	name = "ABC";
	// printf("お名前は？\n");
	// scanf("%s", name);  エラー。ポインタ変数に文字列リテラルを直接設定すると、変更（上書き）ができない
	printf("こんにちは%sさん\n", name);
	return 0;
}