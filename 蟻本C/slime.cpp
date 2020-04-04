#include <stdio.h>
#define MAX_N 100000

int main()
{
	int N;
	char S[MAX_N];
	int ans = 0;

	scanf("%d", &N);
	scanf("%s", S);

	char c = '0';

	for (int i = 0; i < N; ++i)
	{
		if (c == S[i])
		{
			continue;
		}

		else if (i == N-1)
		{
			ans++;
		}

		else
		{
			c = '0';
			ans++;
			if (S[i] == S[i+1])
			{
				c = S[i];
			}
		}
	}

	printf("%d\n", ans);
	return 0;
}


