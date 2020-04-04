def bingo_search(CARD):
    for i in range(3):
        # 横一列そろったか否か
        if CARD[i][0] == '☓' and CARD[i][1] == '☓' and CARD[i][2] == '☓':
            return True

    for j in range(3):
        # 縦一列そろったか否か
        if CARD[0][j] == '☓' and CARD[1][j] == '☓' and CARD[2][j] == '☓':
            return True

    # ななめ一列そろったか否か
    if CARD[0][0] == '☓' and CARD[1][1] == '☓' and CARD[2][2] == '☓':
            return True

    # ななめ一列そろったか否か
    if CARD[0][2] == '☓' and CARD[1][1] == '☓' and CARD[2][0] == '☓':
            return True

    return False



A1 = list(input().split())
A2 = list(input().split())
A3 = list(input().split())
A = [A1, A2, A3]  #Bingoカードが完成
#print(A)

N = int(input())
for i in range(N):
    flag = False
    b = input()
    for j in range(3):
        for k in range(3):
            if A[j][k] == b:
                A[j][k] = '☓'
                flag = True
                break
        if flag == True:
            break
#print(A)

if bingo_search(A):
    print("Yes")

else:
    print("No")
