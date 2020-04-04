#include <iostream>
using namespace std;
#define MAX_N 100000
#define MAX_K 100000

int n;
int K;
int a[MAX_N];
int m[MAX_N];

int dp[MAX_K + 1];

void solve()
{
	memset(dp, -1, sizeof(dp));
	dp[0] = 0;
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j <= K; ++j)
		{
			if (dp[j] >= 0) //i番目まででKが完成している場合
			{
				dp[j] = m[i];
			}

			else if (j < a[i] || dp[j-a[i]] <= 0)
			{
				dp[j] = -1;
			}

			else
			{
				dp[j] = dp[j-a[i]] - 1;
				
			}
			printf("%d, %d ,%d  %d\n",i , j, dp[j], a[i]);
		}
	}

	
	for (int j = 0; j <= K; ++j)
	{
		printf("%d  ", dp[j]);
	}
	printf("\n");
	

	if (dp[K] >= 0)
	{
		printf("Yes\n");
	}

	else
	{
		printf("No\n");
	}
}

int main(int argc, char const *argv[])
{
	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
	{
		scanf("%d", &a[i]);	
	}
	for (int i = 0; i < n; ++i)
	{
		scanf("%d", &m[i]);
	}
	scanf("%d", &K);
	solve();

	return 0;
}