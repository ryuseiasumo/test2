#include <stdio.h>
#include <string.h>

#define N 10
#define M 12

int a[N][M] = {{1,0,0,0,0,0,0,0,0,1,1,0},
			   {0,1,1,1,0,0,0,0,0,1,1,1},
			   {0,0,0,0,1,1,0,0,0,1,1,0},
			   {0,0,0,0,0,0,0,0,0,1,1,0},
		       {0,0,0,0,0,0,0,0,0,1,0,0},
			   {0,0,1,0,0,0,0,0,0,1,0,0},
			   {0,1,0,1,0,0,0,0,0,1,1,0},
		       {1,0,1,0,1,0,0,0,0,0,1,0},
		       {0,1,0,1,0,0,0,0,0,0,1,0},
			   {0,0,1,0,0,0,0,0,0,0,1,0}};
			   
int look[N][M];


bool dfs(int i,int j)
{
	if (look[i][j] == 1)
	{
		return false;
	}

	else
	{
		if (a[i][j] == 1)
		{
			look[i][j] = 1;

			if (i != 0)
			{
				dfs(i-1,j);
				if (j != 0)
				{
					dfs(i-1,j-1);
				}

				if (j != M-1)
				{
					dfs(i-1,j+1);
				}
			}

			if (i != N-1)
			{
				dfs(i+1,j);
				if (j != 0)
				{
					dfs(i+1,j-1);
				}

				if (j != M-1)
				{
					dfs(i+1,j+1);
				}
			}

			if (j != 0)
				{
					dfs(i,j-1);
				}

				if (j != M-1)
				{
					dfs(i,j+1);
				}
			return true;
		}

		else
		{
			return false;
		}
	}
}


int solve(int N_1,int M_1)
{
	int cnt = 0;
	for (int i = 0; i < N_1; ++i)
	{
		for (int j = 0; j < M_1; ++j)
		{
			if(dfs(i,j))
			{
				cnt += 1;
			}	
		}
	}

	return cnt;
}


void print()
{
	printf("オリジナル\n");
	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < M; ++j)
		{
			printf("%d", a[i][j]);
		}
		printf("\n");
	}
	printf("\n");
	printf("参照&書き込み用\n");
	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < M; ++j)
		{
			printf("%d", look[i][j]);
		}
		printf("\n");		
	}
	printf("\n");
}



int main(void)
{
	memset(look, 0, sizeof(look));
	//初期状態出力
	printf("【初期状態】\n");
	print();

	printf("水溜りの数=%d\n\n", solve(N,M));

	printf("【最終状態】\n");
	//最終状態出力
	print();

	return 0;
}