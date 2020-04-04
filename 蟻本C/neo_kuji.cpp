#include <stdio.h>

#define  MAX_N 50


bool search(int K[], int left, int right, int n, int m, int k[])
{
	bool flag = false;

	int harf = (left + right)/2;

	for (int a = 0; a < n; ++a)
	{
		for (int b = 0; b < n; ++b)
		{
			if (K[harf] == (m - k[a] - k[b]))
			{
				flag = true;
				return flag;
			}

			else if (K[harf] > (m - k[a] - k[b]))
			{
				search(K, left, harf, n , m, k);
			}

			else
				search(K, harf ,right, n, m, k);
			
		}
	}

	return flag;
}

void quicksort(int a[], int left, int right, int n)
{
	int pivot = left + (right+1-left)/2;
	int i = left, j = right;

	printf("left = %d : right = %d : pivot = %d\n", left,right,pivot);

	while (i < j)
	{
		int l, r;
		bool l_bool = false;
		bool r_bool = false;

		//今回はa[pivot]と同じ値の場合は、左に来るようにしている
		if (a[i] > a[pivot] || i == pivot)
		{
			l = a[i];
			l_bool = true;
		}

		if (a[j] <= a[pivot])
		{
			r = a[j];
			r_bool = true;
		}

		if (l_bool && r_bool)
		{
			a[i] = r;
			a[j] = l;
			puts("【入れ替え】");

			for (int x = 0; x < n; ++x)
			{
				printf("%d,", a[x]);
			}

			puts("");

			// pivot「a[i]」がa[j]と入れ替わった場合、a[j]をpivotに修正する.さらにjは末尾で-1されるので、+1をここでしておいて、次のループでもa[pivot]が参照されるようにしておく
			if (i == pivot)
			{
				pivot = j;
				j++;
			}

			// pivot「a[j]」がa[i]と入れ替わった場合、a[i]をpivotに修正する.さらにiは末尾で+1されるので、-1をここでしておいて、次のループでもa[pivot]が参照されるようにしておく
			else if (j == pivot)
			{
				pivot = i;
				i--;
			}

			i++;
			j--;
		}

		// a[i]がa[pivot]以下、a[j]がa[pivot]よりも大きい
		else if (l_bool == false && r_bool == false)
		{
			puts("【左 +1、右 -1】");
			i++;
			j--;
		}

		//a[i]がa[pivot]より大きく、a[j]がa[pivot]よりも大きい → a[i]とa[j-1]をa[pivot]と比較
		else if (l_bool && r_bool == false)
		{
			puts("【右 -1】");			
			j--;
		}

		//a[i]がa[pivot]より小さく、a[j]がa[pivot]以下 → a[i+1]とa[j]をa[pivot]と比較
		else
		{
			puts("【左 +1】");
			i++;
		}


	}

	if (left < right)
	{
		// 左半分(pivotを含まない)
		quicksort(a, left, pivot-1, n);
		// 右半分(pivotも含む)
		quicksort(a, pivot, right, n);
	}

	
}


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

	int K[n*n];
	for (int c = 0; c < n; ++c)
	{
		for (int d = 0; d < n; ++d)
		{
			K[c*n+d] = k[c]+k[d];
		}
	}

	quicksort(K, 0, n*n-1, n*n);

	for (int i = 0; i < n*n; ++i)
	{
		printf("%d\n", K[i]);	
	}



	bool flag;

	flag = search(K, 0 ,n*n, n, m ,k);


	if (flag)
	{
		puts("YES");
	}
	else
		puts("NO");


	return 0;
}



