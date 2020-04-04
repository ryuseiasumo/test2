N = int(input())
list = list(map(int,input().split()))
josu = 0

#脳筋
for i in range(len(list)):
    josu += 1/list[i]

ans = 1/josu


#ちょい工夫？
# all_jousu = 1
# for i in range(len(list)):
#     all_jousu *= list[i]
#
# josu = 0
# for i in range(len(list)):
#     josu += all_jousu/list[i]
#
# ans = all_jousu/josu



print(ans)