sz = 0
heap = []

def push(x,sz,heap):
    i = sz
    heap.append(x) #i番目のノードを作成。値は17行目でどうせ入れるのでなんでもいいが、とりあえず確実なxにしておく
    while i > 0:
        #親のノード番号
        p = int((i-1)/2)

        if heap[p] <= x:
            break

        heap[i] = heap[p]
        i = p

    heap[i] = x
    sz += 1

    return (heap,sz)


def pop(heap,sz):
    sz -= 1
    ret = heap[0]  #最小値
    x = heap.pop(sz)
    i = 0
    while (i*2+1 < sz):
        #子同士を比較。左しかない場合は、何もしない
        a = i*2+1
        b = i*2+2
        if b < sz and heap[b] < heap[a]:
            a = b

        #逆転がないなら終わり
        if heap[a] >= x:
            break

        heap[i] = heap[a]
        i = a

    heap[i] = x

    return (ret,heap,sz)


if __name__ == "__main__":
    tuple = push(5,sz,heap)
    sz = tuple[1]
    print(tuple)
    tuple = push(10,sz,heap)
    sz = tuple[1]
    print(tuple)
    tuple = push(32,sz,heap)
    sz = tuple[1]
    print(tuple)
    tuple = push(3,sz,heap)
    sz = tuple[1]
    print(tuple)
    tuple = push(54,sz,heap)
    sz = tuple[1]
    print(tuple)
    tuple = push(2,sz,heap)
    sz = tuple[1]
    print(tuple)
    tuple = push(22,sz,heap)
    sz = tuple[1]
    print(tuple)
    tuple =pop(heap,sz)
    sz = tuple[2]
    print(tuple)

