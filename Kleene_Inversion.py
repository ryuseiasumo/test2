N, K = map(int,input().split())
A = list(map(int,input().split()))
mod = 10**9+7

count_1 = 0
count_2 = 0

for i in range(N):
    for j in range(N):
        if(A[i] > A[j]):
            count_2 += 1
            if i < j:
                count_1 += 1

k = (K-1)*K//2
B = count_1 * K + count_2 * k

print(B%mod)




# mod=10**9+7
# n,k=map(int,input().split())
# arr=list(map(int,input().split()))
#
# cnt1=[0]*n
# cnt2=[0]*n
#
# for i in range(n):
#   for j in range(n):
#     if arr[i]>arr[j]:
#       cnt2[i]+=1
#       if i<j:
#         cnt1[i]+=1
#
# ans=0
# for val in cnt1:
#   ans+=val*k
#   ans%=mod
# for val in cnt2:
#   ans+=val*(k*(k-1)//2)
#   ans%=mod
# print(ans)

