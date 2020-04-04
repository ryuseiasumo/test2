from datetime import datetime

def f_1():
    print(datetime.now())

def f_2(x : str):
    print(x)

def f_3(x : int, y: int) -> int:
    return x+y

f_1()

f_2("ああああああ")

a = f_3(4,7)
print(a)
