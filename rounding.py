x, a , *b= [int(i) for i in map(int, input().split())]   #inputはstr型だから,int型に直さないとね→map(int,)で実装
                                                         # *bには第3要素以降の全ての要素がリストとして格納されている

print(x, a, b)

if(x < a):
    print(0)
else:
    print(10)
