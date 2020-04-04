s = set()
s.add(1) ; s.add(2) ; s.add(3)
print("集合s = ", s)

for i in [1,3,5]:
    print("{}はsの要素である：".format(i),i in s)

s = set([i for i in range(1,50) if i % 2 == 0])
print(s)

s = set([1,2,3])
s_prime = set()

for i in [1, 4, 5]:
    s_prime.add(i)
    print(s_prime, "は{1,2,3}の部分集合である：", s_prime < s)

S1 = set([3, 5, 10])
S2 = set([4, 5, 6])

print("S1 U S2 = ", S1.union(S2))
print("S1 ∩ S2 = ", S1.intersection(S2))

S = set([i for i in range(1000)])
print("#S = ", len(S))