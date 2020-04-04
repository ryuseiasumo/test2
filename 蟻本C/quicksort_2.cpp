#include <stdio.h>
#include <stdlib.h>
#define MAX_N 50

// 比較関数
// void *型はポインタだが、型は指定していない。故に(int *)aなどとキャストする必要あり。
int asc(const void *a, const void *b)
{
  return *(int *)a - *(int *)b;
}
        


int main(void)
{
    int n, a[MAX_N];
    printf("n = ");
    scanf("%d", &n);
    for (int i = 0; i < n; ++i)
    {
        printf("a[%d] = ", i);
        scanf("%d", &a[i]);
    }


    puts("【sort前】");
    for (int i = 0; i < n; ++i)
    {
        printf("%d, ", a[i]);
    }
    puts("");


    qsort(a, n, sizeof(int), asc);


    puts("【sort後】");
    for (int i = 0; i < n; ++i)
    {
        printf("%d, ", a[i]);
    }
    puts("");

    


    return 0;
}