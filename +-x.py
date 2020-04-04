A, B = map(int,input().split())

wa = A + B
sa = A - B
seki = A * B

print(max(wa, sa, seki))