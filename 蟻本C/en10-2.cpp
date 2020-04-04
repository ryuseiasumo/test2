#include <stdio.h>

void decrement_date(int *y, int *m, int *d)
{
	char yn;
	if (*d == 1)
	{
		if (*m == 3)
		{
			*m -= 1;
			printf("その年は閏年？(y/n)：");   scanf("%c", &yn);
			if (yn == 'y')
			{
				*d = 29;
			}

			else
			{
				*d = 28;
			}
		}

		else if (*m == 1)
		{
			*y -= 1;
			*m = 12;
			*d = 31;
		}

		else if (*m == 5 || *m == 7 || *m == 10 || *m == 12)
		{
			*m -= 1;
			*d = 30;
		}

		else
		{
			*m -= 1;
			*d = 31;		
		}
	}

	else
	{
		*d -= 1;
	}
}


void increment_date(int *y, int *m, int *d)
{
	char yn;

	if (*m == 2 && *d == 28)
	{
		printf("その年は閏年？(y/n)：");   scanf("%c", &yn);

		if (yn == 'y')
		{
			*d += 1;
		}

		else
		{
			*m += 1;
			*d = 1;
		}
	}

	else if (*m == 2 && *d == 29)
	{
		*m += 1;
		*d = 1;
	}

	else if (*d == 31)
	{
		if (*m == 12)
		{
			*y += 1;
			*m = 1;
			*d = 1;
		}

		else
		{
			*m += 1;
			*d = 1;
		}
	}

	else if (*d == 30)
	{
		if (*m == 4 || *m == 6 || *m == 9 || *m == 11)
		{
			*m += 1;
			*d = 1;
		}

		else
		{
			*d += 1;
		}
	}

	else
	{
		*d += 1;
	}
}

int main(void)
{
	int y, m ,d;
	char id;

	printf("年：");   scanf("%d", &y);
	printf("月：");   scanf("%d", &m);
	printf("日：");   scanf("%d", &d);
	printf("前の日？後ろの日？(d/i):");  scanf("%c", &id);
	puts("");

	if (id == 'd')
	{
		decrement_date(&y, &m, &d);
		printf("前の日は、%d年%d月%d日\n", y, m, d);
	}

	else
	{
		increment_date(&y, &m, &d);
		printf("後ろの日は、%d年%d月%d日\n", y, m, d);
	}



	return 0;
}