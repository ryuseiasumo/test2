#include <stdio.h>

char name_1[20];
char *name_2;


int main(int argc, char const *argv[])
{
	scanf("%s", name_1);
	//name_1 = "ryusei";は不可
	name_2 = "ryusei";
	//scanf("%s",name_2);は不可

	printf("%s\n", name_1);

	int len_1 = (int)sizeof(name_1)/sizeof(char);
	printf("%d\n", len_1);

	int len_2 = (int)sizeof(name_2)/sizeof(char);
	printf("%d\n", len_2);

	for (int i = 0; i < len_1; ++i)
	{
		printf("%c\n", name_1[i]);
	}

		for (int i = 0; i < len_2; ++i)
	{
		printf("%c\n", name_2[i]);
	}
	return 0;
}