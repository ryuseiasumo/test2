#include <stdio.h>

int main(int argc, char const *argv[])
{
	//ファイルへのポインタ型
	FILE *fp;    

	//fopenはポインタを返す。ファイルが見つからなかったら、NULLを返す。
	fp = fopen("abc", "r");

	if (fp == NULL)
	{
		printf("\aファイル\"abc\"をオープンできませんでした。\n");
	}

	else
	{
		printf("\aファイル\"abc\"をオープンしました\n");

		//fpはファイルへのポインタ
		fclose(fp);
	}
	return 0;
}