N, K = map(int,input().split())
S = input()

#180入れ替えの関数
def switch(l, r, S):
    for i in range(r-l):
        if S[l+i] == S[r-i]:
            if S[l+i] == 'R':
                S[l + i] = 'L'
                S[r - i] = 'L'
            else:
                S[l + i] = 'R'
                S[r - i] = 'R'





# for k in range(K):







#幸福の人の数をだす
kohuku = 0
for i in range(N):
    if S[i] == 'L' and i != 0 and S[i-1] == 'L':
        kohuku += 1

    if S[i] == 'R' and i != N-1 and S[i+1] == 'R':
        kohuku += 1

