#include <stdio.h>

int **back;

int main(void)
{
	int *tmp;
	*tmp = 6;
	 /* *back = tmp;   これだとセグフォ*/
	back = &tmp; //これはダイジョブ
	**back = 5;

	printf("%d\n", *tmp);

	return 0;
}