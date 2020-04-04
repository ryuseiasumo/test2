#include <stdio.h>
 
りゅうせいの解答1 
void hikaku(int *h, int *a, int N)
{
	int count = 0;
	for (int i = N-1; i > 0; --i)
	{
		if (h[i] <= h[i-1])
		{
			count++;
			if ((i == 1) && (*a < count))
			{
				*a = count;
			}
		}

		else
		{
			if (*a < count)
			{
				*a = count;
			}

			count = 0;
		}

	}
}

int main(int argc, char const *argv[])
{
	int N;
	scanf("%d", &N);
	int H[N];

	for (int i = 0; i < N; ++i)
	{
		scanf("%d", &H[i]);
	}

	int ans = 0;

	hikaku(H, &ans, N);

	printf("%d\n", ans);

// りゅうせいの解答2
// int main(int argc, char const *argv[])
// {
// 	int N;
// 	scanf("%d", &N);
// 	int H[N];

// 	for (int i = 0; i < N; ++i)
// 	{
// 		scanf("%d", &H[i]);
// 	}

// 	int ans = 0;

// 	int count = 0;
// 	for (int i = N-1; i > 0; --i)
// 	{
// 		if (H[i] <= H[i-1])
// 		{
// 			count++;
// 			if ((i == 1) && (ans < count))
// 			{
// 				ans = count;
// 			}
// 		}

// 		else
// 		{
// 			if (ans < count)
// 			{
// 				ans = count;
// 			}

// 			count = 0;
// 		}

// 	}

// 	printf("%d\n", ans);

	

// 別解
// int main(void) 
// {
//     int n, count = 0, max = 0;
//     scanf("%d", &n);
//     int h[n];
//     for(int i = 0; i < n; i++) {
//         scanf("%d", &h[i]);
//         if(i > 0) {
//             if(h[i-1] >= h[i]) {
//                 count++;
//             } else {
//                 if(max < count) {
//                     max = count;
//                 }
//                 count = 0;
//             }
//         }
//     }
//     if(max < count) max = count;
//     printf("%d\n", max);
//     return 0;
// }


	return 0;
}