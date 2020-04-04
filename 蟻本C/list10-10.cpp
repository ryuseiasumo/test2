#include <stdio.h>

//vの型は、配列ではなくて、ポインタ
void ary_set(int v[], int n, int val)
{
	int i;
	for (int i = 0; i < n; ++i)
	{
		v[i] = val;
	}
}

int main(int argc, char const *argv[])
{
	int i;
	int a[] = {1, 2, 3, 4, 5};
	ary_set(a, 5, 99);

	for (int i = 0; i < 5; ++i)
	{
		printf("a[%d] = %d\n", i, a[i]);
	}
	return 0;
}