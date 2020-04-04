A, B = map(int,input().split())
Socket = 0
kuchi = 1

while kuchi < B:
    Socket += 1
    kuchi += (A - 1)

print(Socket)