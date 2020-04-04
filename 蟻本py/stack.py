#スタック
stack = [1,2,3]
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)

#キュー
from collections import deque
queue = deque([1,2,3])
print(queue)
queue.append(4)
print(queue)
queue.popleft()  #popleftはdequeを使わないとだめ！
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)

