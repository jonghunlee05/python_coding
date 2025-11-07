import heapq

stones = [2,7,4,1,8,1]

stones = sorted(stones, reverse=True)


print(stones)




while len(stones) > 1:
    l1 = stones.pop(0)
    l2 = stones.pop(0)

    if l1 != l2:
        stones.append(l1 - l2)
        stones = sorted(stones, reverse=True)

print(stones[0])

print(stones)






