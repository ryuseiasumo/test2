// #include <stdio.h>

// int strtoi(const char *nptr)
// {
// 	int *p;
// 	if (*p = int(*nptr))
// 	{
// 		return *p;
// 	}

// 	return 0;
	
// }


// int main(int argc, char const *argv[])
// {
// 	char str = '2';
// 	int i = strtoi(&str); 
// 	printf("%d\n", i);
// 	return 0;
// }

#include <stdio.h>

int strtoi(const char *nptr){

    int num = 0, sign = 1;

    if(*nptr == '+'){
        sign = 1;
        *nptr++;
    }else if(*nptr == '-'){
        sign = -1;
        *nptr++;
    }

    while(true){
        num += *nptr - '0';
        *nptr++;
        if(*nptr == '\0') break;
        num *= 10;
    }

    return num * sign;
}

long strtol(const char *nptr){
   
    int sign = 1;
    long num = 0;

    if(*nptr == '+'){
        sign = 1;
        *nptr++;
    }else if(*nptr == '-'){
        sign = -1;
        *nptr++;
    }

    while(true){
        num += *nptr - '0';
        *nptr++;
        if(*nptr == '\0') break;
        num *= 10;
    }

    return num * sign;
}

double strtof(const char *nptr){
   
    int sign = 1;
    double num = 0;

    // 符号の処理
    if(*nptr == '+'){
        sign = 1;
        *nptr++;
    }else if(*nptr == '-'){
        sign = -1;
        *nptr++;
    }

    // 整数部の処理
    while(true){
        num += *nptr - '0';
        *nptr++;
        if(*nptr == '\0' || *nptr == '.') break;
        num *= 10;
    }

    // 小数部の処理
    if(*nptr == '.'){
        *nptr++;
        double dec = 1;
        while(true){
            num += (*nptr - '0') / (dec *= 10);
            *nptr++;
            if(*nptr == '\0') break;
        }
    }

    return num * sign;
}

int main(){

    char str1[256] = "12345";
    char str2[256] = "123.45";

    printf("str1:%s -> atoi(str1):%d\n", str1, strtoi(str1));
    printf("str1:%s -> atol(str1):%ld\n", str1, strtol(str1));
    printf("str2:%s -> atof(str2):%lf\n", str2, strtof(str2));

    return 0;
}