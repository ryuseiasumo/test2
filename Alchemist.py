N = int(input())
list = list(map(int,input().split()))

list.sort(reverse = True)

while(len(list) > 1):
    vj = list.pop()
    vi = list.pop()
    vk = (vi + vj)/2
    list.append(vk)
    list.sort(reverse = True)

print(list[0])

