from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()
print(queue)
#输出: 'Eric'
queue.popleft()                 # 队首元素出队
print(queue)
#输出: 'John'
queue                           # 队列中剩下的元素
print(queue)
#输出: deque(['Michael', 'Terry', 'Graham'])
