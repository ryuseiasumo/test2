#include <stdio.h>

void sum_diff(int n1, int n2, int *sum, int *diff)
{
	*sum = n1 + n2;
	*diff = (n1 > n2) ? n1 - n2 : n2 - n1;
	printf("*sumと*diffのアドレス：%p %p\n", sum, diff);

}

int main(void)
{
	int n1, n2;
	int wa = 0, sa = 0;

	printf("waとsaのアドレス：%p %p\n", &wa, &sa);

	puts("2つの整数を入力してください");
	printf("整数A:");   scanf("%d", &n1);
	printf("整数B:");   scanf("%d", &n2);

	sum_diff(n1, n2, &wa, &sa);

	printf("和は%dで、差は%d\n", wa, sa);

	return 0;
}