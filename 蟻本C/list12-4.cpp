#include <stdio.h>

#define NAME_LEN 64

struct student
{
	char name[NAME_LEN];
	int height;
	float weight;
	long schols;
};

void hiroko(struct student *std)
{
	if (std -> height < 180)
	{
		std -> height = 180;
	}

	if (std -> weight > 80)
	{
		std -> weight = 80;
	}
	// if ((*std).height < 180)
	// {
	// 	(*std).height = 180;
	// }

	// if ((*std).weight > 80)
	// {
	// 	(*std).weight = 80;
	// }
}

int main(int argc, char const *argv[])
{
	struct student sanaka = {"さなか", 175, 62.5, 73000};

	hiroko(&sanaka);
	printf("%d\n", sanaka.height);

	return 0;
}