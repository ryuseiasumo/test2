#include <iostream>

using namespace std;
#define MAX_N 20000

int N;
int L[MAX_N];

int main(int argc, char const *argv[])
{
	scanf("%d", &N);
	for (int i = 0; i < N; ++i)
		{
			scanf("%d", &L[i]);
		}

	int ans = 0; 
	
	while (N > 1)
	{
		int mil1 = 0, mil2 = 1;
		if (L[mil1] > L[mil2])
		{
			swap(mil1,mil2);
		}
		for (int i = 2; i < N; ++i)
		{
			if (L[i] <= L[mil1]) 
			{
				mil2 = mil1;
				mil1 = i;
			}

			else if (L[i] < L[mil2])
			{
				mil2 = i;
			}
		}

		L[mil1] = (L[mil1] + L[mil2]);
		ans += L[mil1];

		if (mil2 != N-1)
		{
			swap(L[mil2], L[N-1]);
		}

		N--;

	}

	printf("%d\n", ans);

	return 0;
}