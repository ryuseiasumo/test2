# s = int(input())
#
# for i in range(1,s):
#     a = i
#     b = int(s/a)
#     if (s%a == 0 and b <= 10^9):
#         break
#
# x1, y1 = 0, 0
# x2, y2 = a, 0
# x3, y3 = a, b
#
# print(x1, y1, x2, y2, x3, y3)


S = int(input())

x1 = 1
y1 = 10 ** 9
x2 = (S + (10 ** 9 - 1)) // (10 ** 9)
y2 = 10 ** 9 * x2 - S
x3 = 0
y3 = 0

print(x1, y1, x2, y2, x3, y3)