#include <stdio.h>
#include <math.h>

#define sqr(n) ((n)*(n))

typedef struct 
{
	double x;
	double y;
} Point;

double distance_of(Point pa, Point pb)
{
	return sqrt(sqr(pa.x - pb.x) + sqr(pa.y - pb.y));
}

int main(int argc, char const *argv[])
{
	Point crnt, dest;

	printf("現在地のX座標：");    scanf("%lf", &crnt.x);
	printf("現在地のY座標：");    scanf("%lf", &crnt.y);
	printf("目的地のX座標：");    scanf("%lf", &dest.x);
	printf("目的地のY座標：");    scanf("%lf", &dest.y);

	printf("距離は、%.2fです\n", distance_of(crnt, dest));

	return 0;
}