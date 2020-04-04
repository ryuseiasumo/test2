#include <stdio.h>

int main(int argc, char const *argv[])
{
	FILE *fp; 
	char f_name[128];
	puts("ファイル名を入力してください");
	scanf("%s", f_name);

	fp = fopen(f_name, "w");
	fclose(fp);


	return 0;
}