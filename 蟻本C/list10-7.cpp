#include <stdio.h>

void swap(int *px, int *py)
{
	int temp = *px;
	*px = *py;
	*py = temp;
}

void sort2(int *n1, int *n2)
{
	if (*n1 > *n2)
		swap(n1, n2);
	
}

int main(void)
{
	int na, nb;

	puts("2つの整数を入力してください。");
	printf("整数A：");    scanf("%d", &na);
	printf("整数B：");    scanf("%d", &nb);

	sort2(&na, &nb);

	puts("昇順にソートしました。");
	printf("整数Aは%dです。\n", na);
	printf("整数Bは%dです。\n", nb);

	return 0;
}