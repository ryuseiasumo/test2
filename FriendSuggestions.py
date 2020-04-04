import sys
sys.setrecursionlimit(10 ** 7)

class UnionFind():
    def __init__(self, n):
        self.n = n #要素数
        self.parents = [-1] * n #親格納配列(親のときは下流の要素数のマイナスを返す)

    def find(self,x):
        if self.parents[x] < 0: #親のとき
            return x
        else:
            self.parents[x] = self.find(self.parents[x]) #再帰で親に繋ぎ変える
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y: #親が同じときスキップ
            return

        if self.parents[x] > self.parents[y]: #要素数が多いほうをxにする
            x, y = y, x

        self.parents[x] += self.parents[y] #xの要素数はyの要素数ぶん増える
        self.parents[y] = x #yをxの子にする

    def size(self, x): #xの属するグループの要素数
        return -self.parents[self.find(x)]

    def same(self, x, y): #同じグループか判定
        return self.find(x) == self.find(y)

    def members(self, x): #xの属するグループの要素一覧
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self): #根の一覧
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self): #グループ個数
        return len(self.roots())

    def all_group_members(self): #根とその要素の辞書配列
        return {r: self.members(r) for r in self.roots()}

    def __str__(self): #print用
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


n,m,k=map(int,input().split())

U=UnionFind(n)
M=[[] for i in range(n)]
K=[[] for i in range(n)]

for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    U.union(a,b)
    M[a].append(b)
    M[b].append(a)

for i in range(k):
    a,b=map(int,input().split())
    a-=1
    b-=1
    if U.same(a,b):
        K[a].append(b)
        K[b].append(a)

ans=[]
for i in range(n):
    m=M[i]
    k=K[i]
    ans.append(U.size(i)-len(m)-len(k)-1)
print(*ans)
