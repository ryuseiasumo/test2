#include <stdio.h>

int main(void)
{
	char a[11]= "hataryusei";

	char *t = a;
	char *h;
	h  = &a[0];

	printf("ポインタは、%pです\n", a);
	printf("%c\n", a[0]);
	printf("ポインタは、%pです\n", t);
	printf("ポインタは、%pです\n", h);

	return 0;
}