# from math import ceil
# A, B = map(int,input().split())

# def non_taxed_price_8(x):
#     min_8 = x/0.08
#     Max_8 = (x+1)/0.08
#     eight = set(range(ceil(min_8), ceil(Max_8)))
#     return eight

# def non_taxed_price_10(x):
#     min_10 = x/0.1
#     Max_10 = (x+1)/0.1
#     ten = set(range(ceil(min_10), ceil(Max_10)))
#     return ten

# a = non_taxed_price_8(A)
# b = non_taxed_price_10(B)

# r = a&b
# if len(r) == 0:
#     print(-1)
# else:
#     print(min(list(r)))

from math import ceil
A, B = map(int, input().split())

min_8 = ceil(A / 0.08)
max_8 = ceil((A+1) / 0.08)

min_10 = ceil(B / 0.1)
max_10 = ceil((B+1) / 0.1)

ans = -1

for i in range(min_8,max_8):
    if i in range(min_10,max_10):
        ans = i
        break

print(ans)
