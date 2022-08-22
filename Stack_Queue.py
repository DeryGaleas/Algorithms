from collections import deque


#Stack -> Lifo (Last In, First Out)
Stack = deque()
Stack.append("x")
print(Stack)

#Queue -> Fifo (First In, First Out)
Queue = deque()
Queue.appendleft("x")
print(Stack)