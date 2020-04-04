#include <stdio.h>
#define MAX 10^12


long long int A,B,K;

int main(int argc, char const *argv[])
{
	scanf("%lld", &A);
	scanf("%lld", &B);
	scanf("%lld", &K);

	if (A <= K)
	{
		K = K-A;
		A = 0;

		if (B <= K)
		{
			B = 0;
		}

		else{
			B = B-K;
			K = 0;
		}
	}

	else{
		A = A-K;
		K = 0;
	}

	printf("%lld %lld", A, B);
	return 0;
}



// int main(int argc, char const *argv[])
// {
// 	scanf("%d", &A);
// 	scanf("%d", &B);
// 	scanf("%d", &K);

// 	while(K != 0){
// 		if (A != 0)
// 		{
// 			A--;
// 		}

// 		else{
// 			B--;
// 		}

// 		K--;
// 	}

// 	printf("%d %d", A, B);
// 	return 0;
// }
