#include <iostream>
#include <math.h>


using namespace std;

#define MAX_N 100
#define MAX_V 100

int dp[MAX_N + 1][MAX_N * MAX_V + 1];
int n, W;
int w[MAX_V], v[MAX_N];


int INF = INFINITY;

void solve()
{
	fill(dp[0], dp[0] + MAX_N*MAX_V+1, INF); //最小を出していくため、初期値は無限大にしておく方がいい
	dp[0][0] = 0;
	for (int i = 0; i < n+1; ++i)
	{
		for (int j = 0; j < W+1; ++j)
		{
			printf("%d  ", dp[i][j]);
		}
		printf("\n");
	}


	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j <= MAX_N * MAX_V; j++)
		{
			if (j < v[i])
			{
				dp[i+1][j] = dp[i][j];
			}
			else
			{
				dp[i + 1][j] = min(dp[i][j], dp[i][j - v[i]] + w[i]);
			}
		}
	}

	int res = 0;
	for (int i = 0; i <= MAX_N*MAX_V; i++)
	{
		if (dp[n][i] <= W)
		{
			res = i;
		}
	}

	printf("%d\n", res);
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