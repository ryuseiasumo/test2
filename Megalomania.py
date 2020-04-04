#りゅうせいの解答2 正解
N = int(input())
task_list = [list(map(int, input().split())) for i in range(N)]

task_list.sort(key=lambda task_list: task_list[1])
time = 0
flag = True

for i in range(N):
    x = task_list[i]
    time += x[0]
    if time > x[1]:
        flag = False
        break

if flag:
    print("Yes")

else:
    print("No")

#りゅうせいの解答3  実行時間超過（pop()が原因）
# N = int(input())
# task_list = [list(map(int, input().split())) for i in range(N)]
#
# task_list.sort(key=lambda task_list: task_list[1])
# time = 0
# flag = True
#
# while(len(task_list)):
#     x = task_list.pop(0)
#     time += x[0]
#     if time > x[1]:
#         flag = False
#         break
#
# if flag:
#     print("Yes")
#
# else:
#     print("No")



#りゅうせいの解答1　実行時エラー(exit(1)が原因）、実行時間超過
# N = int(input())
# task_list = [list(map(int,input().split())) for i in range(N)]
#
# task_list.sort(key= lambda task_list: task_list[1])
# time = 0
#
# while(len(task_list)):
#     x = task_list.pop(0)
#     time += x[0]
#     if time > x[1]:
#         print("No")
#         exit(1)
#
#     else:
#         continue
#
# print("Yes")