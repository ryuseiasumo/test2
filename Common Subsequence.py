# 両方の数列から同じ部分列がいくつあるか？
import numpy as np

MOD = 10 ** 9 + 7
N, M = map(int, input().split())
S = input().split()  #リスト
T = np.array(input().split(), dtype=np.int32) #行列　また、dtypeを指定することで、要素のデータ型を指定して確保するメモリ量を調節することができる。正しくNumPy配列のデータ型を指定することでPythonからでもメモリ効率と実行効率の良いコードを実装することができる
#print(S)
#print(T)
dp = np.ones(M + 1, dtype=np.int64)  #np.onesは全要素を1にしている。M+1しているのは、dp[:-1]を使うため
#print(dp)

for s in S:
    #print(dp[1:])
    #print(dp[:-1])
    a=(dp[:-1] * (T == int(s))).cumsum()
    #print(a)
    dp[1:] = ((dp[:-1] * (T == int(s))).cumsum() + dp[1:]) % MOD #dp[1:]はd[1]以降。dp[:-1]は「0番目から後ろから1番目まで」（ちなみにdp[-1]は後ろから0番目の要素）。.cumsum()は要素を足し合わせたものを、配列として出力する。
    #print(dp[1:])

print(dp[M])