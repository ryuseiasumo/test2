#りゅうせいの解答改
time =2
list = [list(map(int, input().split())) for i in range(time)]
print(list)
n, x = [i for i in list[0]]
cnt = 0
cur = 0
for i in range(n):
    if cur <= x:
        cnt += 1
    cur += list[1][i]
if cur <= x:
    cnt += 1

print(cnt)


#りゅうせいの解答
# time = 2
# list = [list(map(int,input().split())) for i in range(time)] #list[0]にnとxが,list[1]にL1~Lnが入る
# n, x = [i for i in list[0]]
#
# y = [0]
# cnt = 1
# for i in range(len(list[1])):
#     y.append(y[i] + list[1][i])
#     if (y[i+1] > x):
#         break
#     cnt += 1
#
#
# print(n)

#他の人の解答
# n, x = map(int, input().split())
# ls = list(map(int, input().split()))
#
# cur = 0  #座標
# cnt = 0  #x以下で跳ねた回数
# for i in range(n):
#     if cur <= x:
#         cnt += 1
#     cur += ls[i] #ls[i] = L[i]
# if cur <= x:
#     cnt += 1
#
# print(cnt)
