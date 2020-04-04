import math
# import heapq

A, B = map(int,input().split())
A_list = []
B_list = []


def sosu(X,list):
    for i in range(int(math.sqrt(X))):
        if (X%(i+1) == 0):
            if (i+1 == int(X/(i+1))):
                list.append(i+1)

            else:
                list.append(i+1)
                list.append(int(X/(i+1)))
    list.sort()
    # heapq.heapify(list)
    print(list)

def hikaku(X_list,Y_list, i, j, n,m, Z_list):
    if i == n or j == m:
        return 0

    elif X_list[i] == Y_list[j]:
        Z_list.append(Y_list[j])
        hikaku(X_list,Y_list, i+1, j+1, n,m, Z_list)

    elif X_list[i] < Y_list[j]:
        hikaku(X_list, Y_list, i+1, j, n,m, Z_list)

    else:
        hikaku(X_list, Y_list, i, j+1, n,m, Z_list)




sosu(A, A_list)
sosu(B, B_list)

koyaku = []
N = len(A_list)
M = len(B_list)
hikaku(A_list,B_list,0,0,N,M,koyaku)
print(koyaku)

j = 2
for i in koyaku:
    if i == 1:
        print(i, end= " ")

    else:
        print(i, end= " ")
        for k in range(len(koyaku)-j):
            if(koyaku[j+k]%i == 0):
                del koyaku[j+k]

