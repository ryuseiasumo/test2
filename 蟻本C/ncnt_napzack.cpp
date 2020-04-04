#include <iostream>
using namespace std;

#define MAX_N 100
#define MAX_W 10000

int dp[MAX_N + 1][MAX_W + 1];
int n, W;
int w[MAX_N], v[MAX_N];

void solve()
{
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j <= W; ++j)
		{
			// dp[i+1][j]：＝i番目までの品物から重さの総和がj以下になるように、選んだ時の価値の総和の最大値
			//具体的にはjは残りの重さの許容量を表している。初期値はW。
			if (j < w[i])   //w[i]がjを超えている。すなわち重さの総和がWを超える。
			{
				dp[i+1][j] = dp[i][j];  //i番目の商品を加えないで次の商品へ
			}

			else
			{
				dp[i+1][j] = max(dp[i][j], dp[i+1][j - w[i]]+v[i]); 
				//i番目のを加えない場合と加える場合で、価値の総和が高い方を選ぶ。
				//dp[i+1][j - w[i]]+v[i]は、i番目の商品を1個追加することで、残りの許容量がj-w[i]となり、価値はv[i]増える。商品は繰り返し選べるので、dp[i+1][j-w[i]]でさらに同じことをすると最終的に、繰り返された回数だけ、商品iの価値*個数が総和に追加される
			}
		}
	}
	printf("%d\n", dp[n][W]);

}


int main(int argc, char const *argv[])
{
	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
	{
		scanf("%d", &w[i]);
		scanf("%d", &v[i]);
	}
	scanf("%d", &W);
	for (int i = 0; i < n+1; ++i)
	{
		for (int j = 0; j < W+1; ++j)
		{
			printf("%d  ", dp[i][j]);
		}
		printf("\n");
	}
	solve();
	for (int i = 0; i < n+1; ++i)
	{
		for (int j = 0; j < W+1; ++j)
		{
			printf("%d  ", dp[i][j]);
		}
		printf("\n");
	}

	return 0;
}