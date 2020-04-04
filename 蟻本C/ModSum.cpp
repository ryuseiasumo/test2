#include <stdio.h>

int main(int argc, char const *argv[])
{
	long int N;
	scanf("%ld", &N);

	long int mod_sum;
	mod_sum = N*(N-1)/2;

	printf("%ld\n", mod_sum);
	return 0;
}