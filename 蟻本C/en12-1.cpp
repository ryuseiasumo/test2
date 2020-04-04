 #include <stdio.h>
 #include <stdlib.h>

struct student
{
	char name[64];
	int height;
	float weight;
	long schols;
};

int main(int argc, char const *argv[])
{
	struct student takao = {"タカオ", 173, 86.2};
	printf("%p\n", &takao.name);
	printf("%p\n", &takao.height);
	printf("%p\n", &takao.weight);
	printf("%p\n", &takao.schols);

	return 0;
}