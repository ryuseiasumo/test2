#include <stdio.h>
#include <stdlib.h>

typedef struct choice
{
	int x;
	struct choice *next;
}Choice;

Choice *head = NULL;


void generate()
{
	for (int i = 0; i < 3; ++i)
	{
	Choice *node = (Choice *) malloc(sizeof(Choice));
	node->x = i+1;
	node->next = NULL;

	if (head == NULL){
		head = node;
	}

	else{
		Choice *p = head;
		while(p->next != NULL)
		{
			p = p->next;
		}
		p->next = node;
	}

	}
}

void delete(int x)
{
	Choice *p = head;
	Choice *pre = head;
	if (p == NULL)
	{
		return;
	}

	if (p->x == x)
	{
		head = p->next;
		free(p);
	}

	else{
		while(p != NULL)
	{
		if(p->x == x)
		{
			pre->next = p->next;
			free(p);
			break;
		}
		pre = p;
		p = p->next;
	}
	}
	
}

void print()
{
	Choice *p = head;
	while(p != NULL)
	{
		printf("%d", p->x);
		p = p->next;
	}
}

int main(int argc, char const *argv[])
{
	generate();
	print();

	int A,B;

	printf("\n");
	scanf("%d", &A);
	scanf("%d", &B);

	delete(A);
	delete(B);

	printf("%d\n",head->x);
 	
	return 0;
}