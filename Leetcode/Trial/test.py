from collections import deque
nums = [1,-1]

q = deque([0])

print(len(q))

q.clear()

print(len(q))


q.append(1)
q.append(2)
q.append(-1)
q.append(4)

print(len(q))
print(q)


if  q[2] < 0:
    q.popleft()
    
print(q)


