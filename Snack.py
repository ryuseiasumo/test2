def gcd(a,b):
    if (a % b) == 0:
        return b
    else:
        return gcd(b, a%b)


def lcm(a, b):
    y = gcd(a,b)
    if (y == 0):
        return a*b

    else:
        return a*b/y


A, B = map(int,input().split())
if A < B:
    t = A
    A = B
    B = t

#最小公倍数
x  = int(lcm(A,B))
print(x)

