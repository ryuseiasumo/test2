#include <stdio.h>

void swap(int *px, int *py)
{
	int temp = *px;
	*px = *py;
	*py = temp;
}

int main(void)
{
	int na, nb;

	puts("2つの数字を入れてください");
	printf("1つめ：");    scanf("%d", &na);
	printf("2つめ：");    scanf("%d", &nb);

	swap(&na, &nb);

	puts("これらの値を交換しました");
	printf("1つ目：%d\n", na);
	printf("２つ目：%d\n", nb);

	return 0;
}