A = int(input())
B = int(input())

Choice_list = [1,2,3]

if A in Choice_list:
    del Choice_list[Choice_list.index(A)]

if B in Choice_list:
    del Choice_list[Choice_list.index(B)]

print(Choice_list[0])