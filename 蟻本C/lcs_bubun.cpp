#include <iostream>
#include <math.h>
using namespace std;

#define MAX_N 1000

int n;
int a[MAX_N];
int dp[MAX_N];

int INF = INFINITY;

void solve()
{
	fill(dp,dp+n, INF);
	for (int i = 0; i < n; ++i)
	{
		*lower_bound(dp,dp+n,a[i]) = a[i];
	}

	printf("%ld\n", lower_bound(dp,dp + n, INF) - dp);


}
//O(n**2)
// void solve()
// {
// 	int res = 0;
// 	for (int i = 0; i < n; ++i)
// 	{
// 		dp[i] = 1;
// 		for (int j = 0; j < i; ++j)
// 		{
// 			if (a[i] > a[j])
// 			{
// 				dp[i] = max(dp[i], dp[j] + 1);
// 			}
// 		}
// 		res = max(res, dp[i]);
// 	}

// 	printf("%d\n", res);


// }

int main(int argc, char const *argv[])
{
	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
	{
		scanf("%d", &a[i]);	
	}
	solve();

	return 0;
}