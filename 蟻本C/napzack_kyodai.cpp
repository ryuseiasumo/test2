#include <iostream>
#define MAX_N 100
#define MAX_M 4950
#define MAX_W 10000

int n,m,W;
int w[MAX_N], v[MAX_N], a[MAX_M], b[MAX_M];
int w2[MAX_N], v2[MAX_N] , list[MAX_N][MAX_N];
int dp[MAX_N + 1][MAX_W + 1];

int main(int argc, char const *argv[])
{
	printf("%d\n", list[3][5]);
	list[3] += 5;
	printf("%d\n", list[3][0]);
	return 0;
}

// void solve()
// {
// 	if ()
// 	{
// 		/* code */
// 	}


// 	printf("%d\n", dp[n][W]);
// }

// int main()
// {
// 	scanf("%d", &n);
// 	scanf("%d", &m);
// 	scanf("%d", &W);

// 	for (int i = 0; i < n; ++i)
// 	{
// 		scanf("%d", &w[i]);
// 		scanf("%d", &v[i]);
// 	}

// 	for (int i = 0; i < m; ++i)
// 	{
// 		scanf("%d", &a[i]);
// 		scanf("%d", &b[i]);
// 	}


// 	for (int i = 0; i < m; ++i)
// 	{
// 		for (int j = 0; j < N; ++j)
// 		{
// 			/* code */
// 		}
// 	}


// 	solve();
// 	for (int i = 0; i < n+1; ++i)
// 	{
// 		for (int j = 0; j < W+1; ++j)
// 		{
// 			printf("%d  ", dp[i][j]);
// 		}
// 		printf("\n");
// 	}

// 	return 0;

// }