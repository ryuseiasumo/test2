#include <stdio.h>

int socket = 0;
int kuchi = 1;

void setuzoku(int *x, int *y, int a)
{
	*x += 1;
	*y += a - 1;
}

int main(int argc, char const *argv[])
{
	int a, b;
	scanf("%d%d", &a, &b);

	while (kuchi < b)
	{
		setuzoku(&socket, &kuchi, a);
	}

	printf("%d\n", socket);

	return 0;
}