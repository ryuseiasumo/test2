#include <stdio.h>
#include <string.h>

#define NUMBER 5
#define NAME_LEN 64

typedef struct student 
{
	char name[NAME_LEN];
	int height;
	float weight;
	long schols;
} Student;


void swap_Student(Student *x, Student *y)
{
	Student temp = *x;
	*x = *y;
	*y = temp;
}

void sort_by_height(Student a[], int n)
{
	int i , j;

	for (int i = 0; i < n - 1; ++i)
	 {
	 	for (int j = n - 1; j > 0 ; --j)
	 	{
	 		if (a[j-1].height > a[j].height)
	 		{
	 			swap_Student(&a[j-1], &a[j]);
	 		}
	 	}
	 } 
}


int main(){

    int i, n;

    Student std[256];

    printf("何人の情報を入力しますか？");    scanf("%d", &n);

    for(i = 0; i < n; i++){
        printf("氏名 : "); scanf("%s", std[i].name);
        printf("身長 : "); scanf("%d", &std[i].height);
        printf("体重 : "); scanf("%f", &std[i].weight);
        printf("奨学金 : "); scanf("%ld", &std[i].schols);
    }

    printf("身長を昇順にソート:1, 名前を昇順にソート:2 -> "); scanf("%d", &i);

    if(i == 1){
        sort_by_height(std, n);
        printf("身長順にソートしました\n");
    }
    else if(i == 2){
        sort_by_name(std, n);
        printf("名前順にソートしました\n");
    }

    for(i = 0; i < n; i++){
        printf("%-8s %6d%6.1f%7ld\n", std[i].name, std[i].height, std[i].weight, std[i].schols);
    }

    return 0;
}