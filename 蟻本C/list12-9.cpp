#include <stdio.h>
#include <math.h>

#define sqr(n) ((n)*(n))

//点の座標を表す構造体
typedef struct 
{
	double x;
	double y;
} Point;

//自動車を表す構造体
typedef struct 
{
	Point pt;
	double fuel;
} Car;



double distance_of(Point pa, Point pb)
{
	return sqrt(sqr(pa.x - pb.x) + sqr(pa.y - pb.y));
}

void put_info(Car c)
{
	printf("現在位置:(%.2f,%.2f)\n", c.pt.x, c.pt.y);
	printf("残り燃料：%.2fリットル\n", c.fuel);
}

int move(Car *c, Point dest)
{
	double d = distance_of(c -> pt, dest);
	if (d > c -> fuel)
	{
		return 0;
	}

	c -> pt = dest;
	c -> fuel -= d;

	return 1;
}





int main(int argc, char const *argv[])
{
	Car mycar = {{0.0,0.0},90.0};
	while(1)
	{
		int select;
		Point dest;
		put_info(mycar);
		printf("移動しますか？【Y...1/N...0】：");    scanf("%d", &select);
		if (select != 1)
			break;
		printf("目標値のX座標；");   scanf("%lf", &dest.x);
		printf("目標値のY座標；");   scanf("%lf", &dest.y);

		if (!move(&mycar, dest))
		{
			puts("燃料不足で移動不可");
		}
	}

	return 0;
}