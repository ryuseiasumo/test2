#include <stdio.h>
#include <string.h>

#define MAX_NAME 10
#define NUMBER 5

typedef struct 
{
	char name[MAX_NAME+1];
	int height;
	int weight;
	int schols;
}Student;

typedef enum
{
	Append, //0
	Delete, //1
	Finish //2
}Command;

Command select_command(void)
{
	int num;
	do{
		puts("0:append, 1:delete, 2:finish");
		scanf("%d", &num);
	}while(num < Append || num > Finish);
	return num;
}

Student std[];
int length = 0;

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
			if ((a+j-1)->height > (a+j)->height)  //アロー演算子(a[j-1].height > a[j].heightと同じ)
			{
				swap_student(&a[j-1], &a[j]);
			}
		}
	}
}

void append(char *name, int height, int weight, int schols)
{
	strcpy(std[length].name,name);
	std[length].height = height;
	std[length].weight = weight;
	std[length].schols = schols;
	length++;
}

void delete(int idx)
{
	if (idx == length-1)
	{
		length--;
	}

	else
	{
		swap_student(&std[idx],&std[length-1]);
		length--;
	}
}

int main(int argc, char const *argv[])
{
	char name[MAX_NAME+1];
	int height;
	int weight;
	int schols;
	Command selected;
	int idx;

	do {
		switch (selected = select_command())
		{
			case Append:
						printf("名前：");
						scanf("%s", name);
						printf("身長(整数で)：");
						scanf("%d", &height);
						printf("体重(整数で)：");
						scanf("%d", &weight);
						printf("奨学金：");
						scanf("%d", &schols);
						append(name, height, weight, schols);
						break;
			case Delete:
						printf("消す要素:");
						scanf("%d", &idx);
						delete(idx);
						break;
		}

	}while(selected != Finish);


	int i;
	for (i = 0; i < length; ++i)
	{
		printf("%-8s %6d%6ld%7ld\n", std[i].name, std[i].height, std[i].weight, std[i].schols);
	}

	sort_by_height(std, length);

	puts("ソート後");
	for (i = 0; i < length; ++i)
	{
		printf("%-8s %6d%6d%7ld\n", std[i].name, std[i].height, std[i].weight, std[i].schols);
	}
	return 0;
}