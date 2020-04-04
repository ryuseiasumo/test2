S = input()
Q = int(input())
rflag = False

for i in range(Q):
    t = input()
    if t[0] == "1":
        if rflag == False:
            rflag = True

        else:
            rflag = False

    else:
        t_2, f, c = t.split()

        if (f == '1' and rflag == False) or (f == '2' and rflag == True):
            S = c + S
        else:
            S = S + c

if rflag == True:
    S = S[::-1]
print(S)


# S = input()
# Q = int(input())

# l = len(S)

# for i in range(Q):
#     t = input()
#     if len(t) == 1:
#         S = S[::-1]

#     else:
#         t_2, f, c = t.split()
#         l += 1

#         if f == '1':
#             S = c + S
#         else:
#             S = S + c
# print(S)
