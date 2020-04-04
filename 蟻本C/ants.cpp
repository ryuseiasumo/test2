#include <stdio.h>
#include <algorithm>

#define MAX_N 50

int main(void)
{
	int L, n , x[MAX_N];

	puts("竿の長さ");
	scanf("%d", &L);

	puts("ありの数");
	scanf("%d", &n);

	for (int i = 0; i < n; ++i)
	{
		printf("あり%d匹目の位置", i);
		scanf("%d", &x[i]);
	}

	//最小は、すべてのありが、近い方に向かう時
	int minT = 0;
	for (int i = 0; i < n; ++i)
	{
		//min(x[i], L-x[i])で近い方を選択。max(minT,〜〜)で一番遅く落ちるありを更新していく
		minT = std::max(minT, std::min(x[i], L-x[i]));
	}


	//最大は、すべてのありが、遠い方に向かう場合
	int maxT = 0;
	for (int i = 0; i < n; ++i)
	{
		maxT = std::max(maxT, std::max(x[i],L-x[i]));
	}

	printf("%d %d\n", minT, maxT);
	return 0;
}