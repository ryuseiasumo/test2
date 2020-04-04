// #include <stdio.h>
// #define MAX_N 10^5

// int N,K;
// int R,S,P;
// int dp[MAX_N+1];

// int max(int gu, int tyoki, int par){
// 	if (gu <= tyoki)
// 	{
// 		if (par <= tyoki){
// 			return tyoki;
// 		}

// 		else{
// 			return par;
// 		}
// 	}

// 	else{
// 		if (par <= gu){
// 			return gu;
// 		}

// 		else{
// 			return par;
// 		}

// 	}
// }

// 正解だが実行時間超過する.
// int solve(int i, char *T, char *Takahashi)
// {
// 	if (i == 0)
// 	{
// 		return 0;
// 	}

// 	int gu, tyoki, par;
// 	if (i+K <= N && Takahashi[i+K] == 'r'){ //K手後の自分の手がグー
// 		gu = 0;
// 	}
// 	else{
// 		if (T[i-1] == 's'){ //グーで勝つ
// 			Takahashi[i] = 'r';
// 			gu = solve(i-1, T ,Takahashi) + R;
// 		}
// 		else{ //グーであいこ,または負け
// 			Takahashi[i] = 'r';
// 			gu = solve(i-1, T, Takahashi);
// 		}
		
// 	}

// 	if (i+K <= N && Takahashi[i+K] == 's'){ //K手後の自分の手がチョキ
// 		tyoki = 0;
// 	}
// 	else{
// 		if (T[i-1] == 'p'){ //チョキで勝つ
// 			Takahashi[i] = 's';
// 			tyoki = solve(i-1, T ,Takahashi) + S;
// 		}
// 		else{ //チョキであいこ,または負け
// 			Takahashi[i] = 's';
// 			tyoki = solve(i-1, T, Takahashi);
// 		}
		
// 	}

// 	if (i+K <= N && Takahashi[i+K] == 'p'){ //K手後の自分の手がパー
// 		par = 0;
// 	}
// 	else{
// 		if (T[i-1] == 'r'){ //パーで勝つ
// 			Takahashi[i] = 'p';
// 			par = solve(i-1, T ,Takahashi) + P;
// 		}
// 		else{ //パーであいこ,または負け
// 			Takahashi[i] = 'p';
// 			par = solve(i-1, T, Takahashi);
// 		}
		
// 	}

	

// 	dp[i]= max(gu, tyoki, par);		
	
// 	return dp[i];
// }

// int main(int argc, char const *argv[])
// {
// 	scanf("%d", &N);
// 	scanf("%d", &K);
// 	scanf("%d", &R);
// 	scanf("%d", &S);
// 	scanf("%d", &P);

// 	char T[N];
// 	char Takahashi[N];
// 	scanf("%s", T);

// 	int ans;
// 	ans = solve(N, T, Takahashi);
// 	printf("%d\n", ans);



// 	return 0;
// }


#include<stdio.h>
int main(){
    int n,k;scanf("%d %d",&n,&k);
    int r,s,p;scanf("%d %d %d",&r,&s,&p);
    char t[200000];scanf("%s",t);
 
    int table[200000]={};
    for(int i=0;i<n;i++){
        if(t[i]=='r'){
            table[i]=p;
        }else if(t[i]=='s'){
            table[i]=r;
        }else{
            table[i]=s;
        }
    }
    //for(int i=0;i<n;i++)printf("%d ",table[i]);
    unsigned long long int ans=0;
    for(int i=0;i<k;i++)ans+=table[i];
    for(int i=k;i<n;i++){
        if(t[i]!=t[i-k])ans+=table[i];
        else t[i]='.';
    }
    printf("%llu\n",ans);
    return 0;
}