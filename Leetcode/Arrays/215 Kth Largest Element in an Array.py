import heapq

nums = [3,2,1,5,6,4]
k = 2

heap = []

for n in nums:
    heapq.heappush(heap, n)
    
    print(heap)
    
    if len(heap) > k:
        heapq.heappop(heap)

print(heap[0])
