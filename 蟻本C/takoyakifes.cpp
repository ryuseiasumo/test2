#include <stdio.h>

#define MAX_N 50

int main(int argc, char const *argv[])
{
	int N, d, ans;
	int d_list[MAX_N];

	ans = 0;

	scanf("%d", &N);

	for(int i = 0; i < N; i++)
	{
		scanf("%d", &d_list[i]);
	}

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (i != j)
			{
				d = d_list[i] * d_list[j];
				ans += d;
			}
		}
	}

	ans /= 2;
	printf("%d\n", ans);

}