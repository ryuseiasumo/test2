#include <iostream>
using namespace std;

#define MAX_N 100
#define MAX_W 10000
int n, W;
int w[MAX_N], v[MAX_N];
int dp[MAX_N + 1][MAX_W + 1];  //メモ化テーブル

int rec(int i, int j)
{
	if (dp[i][j] >= 0)
	{
		return dp[i][j];
	}

	int res;
	if (i == n)
	{
		res = 0;
	}
	else if (j < w[i])
	{
		res = rec(i + 1, j);		//再帰//
	}

	else
	{
		res = max(rec(i+1, j) , rec(i+1, j-w[i]) + v[i]);
	}

	return dp[i][j] = res;

}

void solve()
{
	memset(dp, -1 ,sizeof(dp));
	for (int i = 0; i < n+1; ++i)
	{
		for (int j = 0; j < W+1; ++j)
		{
			printf("%d  ", dp[i][j]);
		}
		printf("\n");
	}
	printf("%d\n", rec(0, W));
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