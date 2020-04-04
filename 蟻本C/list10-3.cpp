#include <stdio.h>

int main(void)
{
	int sato = 178;
	int sanaka = 175;
	int masaki = 179;

	//*はポインタ型
	int *isako, *hiroko;

	//&はオブジェクトのアドレスを取り出すアドレス演算子
	isako = &sato;
	hiroko = &masaki;

	printf("イサコさんの好きな人の身長：%d\n", *isako);

	isako = &sanaka;
	printf("イサコさんの好きな人の身長：%d\n", *isako);

	*hiroko = 180;

	printf("ひろ子さんの好きな人の身長：%d\n", *hiroko);
	printf("%p\n", hiroko);
	printf("%p\n", &sanaka);
	printf("%d %d %d\n", sato, sanaka, masaki);


	return 0;
}