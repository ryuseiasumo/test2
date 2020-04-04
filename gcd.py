def gcd(x, y):
    if (x%y == 0):
        return y
    else:
        return gcd(y,x%y)


A, B = map(int,input("A B = ").split())
if A < B:
    t = A
    A = B
    B = t

ans = gcd(A,B)

print(ans)