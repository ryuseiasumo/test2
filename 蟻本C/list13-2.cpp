#include <stdio.h>

int main(int argc, char const *argv[])
{
	FILE *fp;
	int ninzu = 0;
	char name[100];
	double height, weight;
	double hsum = 0.0;
	double wsum = 0.0;

	if ((fp = fopen("hw.dat", "r")) ==  NULL)
	{
		printf("ファイルをオープンできません\n");
	}
	else
	{
		//nemeはもともとアドレスを示している
		while(fscanf(fp ,"%s%lf%lf", name, &height, &weight) == 3)
		{
			printf("%-10s %5.1lf %5.1lf \n", name, height, weight);
			ninzu++;
			hsum += height;
			wsum += weight;
		}

		printf("---------------------------------\n");
		printf("平均     %5.1lf %5.1lf\n", hsum / ninzu, wsum / ninzu);
		fclose(fp);
	}
	return 0;
}