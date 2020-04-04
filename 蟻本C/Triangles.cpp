#include <stdio.h>
#include <stdlib.h>

#define MAX_N 2000

int compare_int(const void *a, const void *b)
{
	return *(int*)a - *(int*)b;
}

int main()
{
	int N, i, j, k, ans = 0;
	int l[MAX_N];
	scanf("%d", &N);
	for (i = 0; i < N; i++)
	{
		scanf("%d", &l[i]);
	}

	qsort(l, N, sizeof(int), compare_int);

	for (i = 0; i < N-2; i++)
	{
		for (j = i+1; j < N-1; j++)
		{
			for (k = j+1; k < N; k++)
			{
				if ((l[i]+l[j]) > l[k])
				{
					ans++;
				}
				else
				{
					break;
				}
			}
		}
	}
	printf("%d\n", ans);
	return 0;
}