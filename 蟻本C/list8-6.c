#include<stdio.h>

// enum animal { Dog, Cat, Monkey, Invalid};

// typedef enum animal { 
// 	Dog, Cat, Monkey, Invalid
// } Animal;

typedef enum { 
	Dog, Cat, Monkey, Invalid
} animal;

void dog()
{
	printf("犬\n");
}

void cat()
{
	printf("猫\n");
}

void monkey()
{
	printf("猿\n");
}

animal serect(void) 
{
	int tmp;
	do{
		puts("0:犬, 1:猫, 2:猿, 3:終了:");
		scanf("%d", &tmp);
	}while(tmp < Dog || tmp > Invalid);
	return tmp;
}

int main(void)
{
	animal selected;
	do{
		selected = serect();
		switch (selected){
			case Dog: 
				dog();
				break;
			case Cat:
				cat();
				break;
			case Monkey:
				monkey();
				break;
		}
	}while(selected != Invalid);

	return 0;
}