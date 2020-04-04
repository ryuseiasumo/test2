#include <stdio.h>
#include <string.h>

#define MAX_NAME 10
#define NUMBER 5

typedef struct 
{
	char name[MAX_NAME+1];   //*nameは？→今回はオッケー(scanfしてないからね)
	int height;
	double weight;
	int schols;
}Student;

void swap_student(Student *x, Student *y)
{
	Student tmp = *x;
	*x = *y;
	*y = tmp;
}

void sort_by_height(Student *a, int n)  //Student a[]でもオッケー
{
	int i,j;
	for (int i = 0; i < n-1; ++i)
	{
		for (int j = n-1; i < j ; j--)
		{
			if (a[j-1].height > a[j].height)
			{
				swap_student(&a[j-1], &a[j]);
			}
		}
	}
}

int main(int argc, char const *argv[])
{
	int i;
	Student std[] = {
		{"Sato", 178, 61.2, 80000},
		{"Sanala", 175, 62.5, 73000},
		{"Takao", 173, 86.2, 0},
		{"Mike", 165, 72.3, 70000},
		{"Masaki", 179, 77.5, 70000}
	};

	for (i = 0; i < NUMBER; ++i)
	{
		printf("%-8s %6d%6.1f%7ld\n", std[i].name, std[i].height, std[i].weight, std[i].schols);
	}

	sort_by_height(std, NUMBER);

	puts("ソート後");
	for (i = 0; i < NUMBER; ++i)
	{
		printf("%-8s %6d%6.1f%7ld\n", std[i].name, std[i].height, std[i].weight, std[i].schols);
	}
	return 0;
}