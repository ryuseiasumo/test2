from collections import deque

S = "aaaiiiiaabbiiii"
T = ""
S_list = deque([i for i in S])
print(S_list)

a = 0
b = len(S_list) - 1

while a <= b:
    left = False
    for i in range(0,b-a):
        if S_list[a+i] < S_list[b-i]:
            left = True
            break

        elif S_list[a+i] > S_list[b-i]:
            left = False
            break

    if left:
        T += S_list.popleft()
        b -= 1

    else:
        T += S_list.pop()
        b -= 1

print(T)




# 隆聖解答（同じのが続いたときうまく行かない）
# def line(S_list, i, j):
#     flag = False
#     if ((S_list[i] == S_list[j]) and i < j):
#         print(S_list[i], S_list[j])
#         line(S_list, i + 1, j - 1)
#
#     elif j <= i:
#         flag = True
#
#     elif (S_list[i] < S_list[j]):
#         print(S_list[i],S_list[j],0)
#         flag = True
#
#     else:
#         print(S_list[i], S_list[j],1)
#
#     return flag
#
#
# while len(S_list):
#     if ((S_list[0] == S_list[len(S_list)-1]) and len(S_list) != 1):
#         if line(S_list,1,len(S_list)-2):
#             T += S_list.popleft()
#
#         else:
#             T += S_list.pop()
#
#     elif (S_list[0] < S_list[len(S_list)-1]):
#         T += S_list.popleft()
#
#     else:
#         T += S_list.pop()
#
# print(T)





