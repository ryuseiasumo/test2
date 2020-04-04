A, B = map(int,input().split())

C = A - B*2
if C<=0:
    print(0)
else:
    print(C)