N, L = map(int,input().split())

A_list = []
aji = 0

for i in range(N):
    A_list.append(L + i)
    aji += (L + i)

#絶対値が0に一番近いものを取り出す
x = min(A_list,key= lambda A_list:abs(A_list))
#print(x)

aji -= x
print(aji)

