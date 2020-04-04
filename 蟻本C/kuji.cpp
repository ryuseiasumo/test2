#include <stdio.h>

#define  MAX_N 50

int main(void)
{
	int n, m, k[MAX_N];
	printf("n = ");
	scanf("%d", &n);
	printf("m = ");
	scanf("%d", &m);
	for (int i = 0; i < n; ++i)
	{
		printf("k[%d] = ", i);
		scanf("%d", &k[i]);
	}

	bool flag = false;

	for (int a = 0; a < n; ++a)
	{
		for (int b = 0; b < n; ++b)
		{
			for (int c = 0; c < n; ++c)
			{
				for (int d = 0; d < n; ++d)
				{
					if ((k[a] + k[b] + k[c] + k[d]) == m)
					{
						flag = true;
					}
				}
			}
		}
	}

	if (flag)
	{
		puts("YES");
	}
	else
		puts("NO");


	return 0;
}