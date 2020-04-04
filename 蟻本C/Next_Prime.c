#include <stdio.h>
#include <stdbool.h>
#include <math.h>

#define MAX 200000 //ベルトラン・チェビシェフの定理より,100000以降の初めの素数は必ず200000以下にあるから.

bool solve(int X);
int X;

int main(int argc, char const *argv[])
{
	scanf("%d", &X);
	for (int i = X; i < MAX; ++i)
	{
		if (solve(i))
		{
			printf("%d\n", i);
			break;
		}
	}

	return 0;
}



bool solve(int X){
	if (X == 2)
	{
		return true;
	}
	
	else if (X%2 == 0)
	{
		return false;
	}

	else{
		int x;
		x = (int)sqrt(X);
		for (int i = 3; i < x+1; i+=2)
		{
			if (X%i == 0)
			{
				return false;
			}
		}

		return true;
	}

}