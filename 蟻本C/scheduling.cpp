#include <iostream>

using namespace std;

const int MAX_N = 100000;

int N;
int S[MAX_N] , T[MAX_N];

pair<int, int> itv[MAX_N];

void solve()
{
	for (int i = 0; i < N; ++i)
	{
		itv[i].first = T[i];
		itv[i].second = S[i];
	}

	sort(itv, itv+N);

	for (int i = 0; i < N; ++i)
	{
		printf("%d %d\n", itv[i].first , itv[i].second);
	}

	int ans = 0, t = 0;
	for (int i = 0; i < N; ++i)
	{
		if (t < itv[i].second)
		{
			ans++;
			t = itv[i].first;
		}
	}

	printf("%d\n", ans);
}

int main(int argc, char const *argv[])
{
	scanf("%d", &N);
	for (int i = 0; i < N; ++i)
	{
		scanf("%d", &S[i]); 

	}
	for (int i = 0; i < N; ++i)
	{
		scanf("%d", &T[i]); 

	}

	solve();

	return 0;
}