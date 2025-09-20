
d = {}
d["a"] = 1
d["b"] = 2
d["c"] = 3

for i in d:
    print(i)

del d["a"]

print(d)

x = d.get("b", 3)
print(x)

print(d["c"])


s = {1,2,3,4,5}


s.add(6)
s.remove(1)
s.discard(2)

print(s)



import heapq

print("heap")

h = []

heapq.heappush(h, 1)
heapq.heappush(h, 2)
heapq.heappush(h, 3)

print(h)

print(heapq.heappop(h))
print(heapq.heappop(h))

print(h)



from collections import deque


l = [1,2,3,4,5]

print(l)
l.pop(2)
print(l)



from collections import deque
q = deque()
q.append(1)      # push right
q.appendleft(2)  # push left
print(q)
q.pop()          # remove right
q.popleft()      # remove left

print(q)





