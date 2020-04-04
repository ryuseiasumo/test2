#include <stdio.h>
#include <stdlib.h>

#define NAME_LEN  64

struct student
{
	char name[NAME_LEN];
	int height;
	float weight;
	long schols;	
};


int main(int argc, char const *argv[])
{
	struct student sanaka;

	strcpy(sanaka.name, "Sanaka");
	sanaka.height = 175;
	sanaka.weight = 62.5;
	sanaka.schols = 73000;

	printf("氏名  = %s\n", sanaka.name);
	printf("身長  = %d\n", sanaka.height);
	printf("体重  = %.1f\n", sanaka.weight);
	printf("奨学金  = %ld\n", sanaka.schols);

	return 0;
}