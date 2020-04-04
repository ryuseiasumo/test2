#include <stdio.h>

struct xyz
{
	int x;
	long y;
	double z;
};

struct xyz xyz_of(int x, long y, double z)
{
	struct xyz temp;

	temp.x = x;
	temp.y = y;
	temp.z = z;
	return temp;
};

int main(int argc, char const *argv[])
{
	struct xyz s = {0, 0, 0};
	s = xyz_of(12, 7654321, 35.689);

	printf("%d\n", s.x);
	return 0;
}