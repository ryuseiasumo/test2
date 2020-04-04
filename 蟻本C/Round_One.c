#include <stdio.h>
#include <stdlib.h>

int choice_list[3] = {1,2,3};
int len = sizeof(choice_list)/sizeof(int);

void delete(int x)
{
	for (int i = 0; i < len; ++i)
	{
		if (x == choice_list[i])
		{
			int tmp;
			tmp = choice_list[i];
			choice_list[i] = choice_list[len-1];
			choice_list[len-1] = tmp;
			len--;
		}
		
	}
	
}

void print()
{
	for (int i = 0; i < len; ++i)
	{
		printf("%d", choice_list[i]);
		printf("\n");
	}
}

int main(int argc, char const *argv[])
{
	int A,B;
	scanf("%d", &A);
	scanf("%d", &B);

	delete(A);
	delete(B);

	printf("%d\n", choice_list[0]);

	return 0;
}