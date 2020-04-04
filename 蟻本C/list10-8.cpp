#include <stdio.h>

void swap(void *px, void *py)
{
	printf("%f\n",*(double *)px);
	int temp = *(int *)px;
	*(int *)px = *(int *)py;
	*(int *)py = temp;
	printf("%f\n",*(double *)py);
}

int main(void)
{
	double da, db;

	puts("2つの実数を入力してください。");
	printf("整数A：");    scanf("%lf", &da);
	printf("整数B：");    scanf("%lf", &db);

	swap(&da, &db);

	puts("値を交換しました。");
	printf("整数Aは%0.2fです。\n", da);
	printf("整数Bは%fです。\n", db);




	return 0;
}