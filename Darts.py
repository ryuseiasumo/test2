# import math
# f_inf_minus = -float('inf')
# print(f_inf_minus)

# N, M = map(int,input().split())

# a = []
# [a.append(int(input())) for i in range(N)]
# a.sort()

# ans = 0

# #全探索(O(n^4))
# # for i in range(N):
# #     for j in range(N):
# #         for k in range(N):
# #             for l in range(N):
# #                 if a[i] + a[j] + a[k] + a[l] <= M:
# #                     if a[i] + a[j] + a[k] + a[l] > ans:
# #                         ans = a[i] + a[j] + a[k] + a[l]

# #二分探索(O(n^3))
# def binary_search(x):
#     l = 0
#     r = N

#     while r - l >= 1:
#         i = (r+l)//2
#         if a[i] == x:
#             return a[i]

#         elif a[i] < x:
#             l = i + 1
#         else:
#             r = i

#     if a[i] > x:
#         i -= 1
#         if a[i] > x and x < 0: # x < 0　は M-y<0 すなわち、M<yの時
#             return -10**10
#         elif a[i] > x: # y<Mの時、すなわち、ダーツをあてず0点にすればいい時
#             return 0

#     return a[i]


# for i in range(N):
#     for j in range(N):
#         for k in range(N):
#             y = a[i]+a[j]+a[k]
#             z = binary_search(M-y)
#             if y+z >= ans:
#                 ans = y+z

# print(ans)



#二分探索(O(n^2log(n^2)))
N, M = map(int,input().split())

a = [0]
[a.append(int(input())) for i in range(N)]
a.sort()

ans = 0

b = []

for i in range(N+1):
    for j in range(N+1):
        b.append(a[i]+a[j])


def binary_search(x):
    l = 0
    r = (N+1)*(N+1)

    while r - l >= 1:
        i = (r+l)//2
        if b[i] == x:
            return b[i]

        elif b[i] < x:
            l = i + 1
        else:
            r = i

    if b[i] > x:
        i -= 1
        if b[i] > x and x < 0: # x < 0　は M-y<0 すなわち、M<yの時
            return -10**10
        elif b[i] > x: # y<Mの時、すなわち、ダーツをあてず0点にすればいい時
            return 0

    return b[i]


for i in range(N):
    for j in range(N):
        y = a[i]+a[j]
        z = binary_search(M-y)
        if y+z >= ans:
            ans = y+z

print(ans)
