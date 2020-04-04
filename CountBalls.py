N, A, B = map(int, input().split())

a = A+B

x = N//a  #繰り返し回数
y = N%a #余り

if y < A:
    b = y
else:
    b = A

blue_count = A * x + b

print(blue_count)
