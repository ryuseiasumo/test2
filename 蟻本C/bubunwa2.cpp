#include <stdio.h>
#define MAX_N 20

int n;
int a[MAX_N];
int k;

bool dfs(int i, int sum, int n,int* a,int k)
{
	if (i == n)
	{
		return sum == k;
	}

	if (dfs(i+1, sum, n, a, k))
	{
		return true;
	}

	if (dfs(i+1, sum+a[i], n, a, k))
	{
		return true;
	}

	return false;
}

void solve(int n,int* a,int k)
{
	int i = 0;
	int sum = 0;
	bool f = dfs(i, sum, n , a, k);
	if (f)
	{
		printf("YES\n");
	}

	else
	{
		printf("NO\n");
	}
}

int main(void)
{
 	scanf("%d", &n);
 	for (int i = 0; i < n; ++i)
 	{
 		scanf("%d", &a[i]);
 	}
 	scanf("%d", &k);
 	solve(n , a, k);
}