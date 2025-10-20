"""
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 
 
we have to use deque. 


1. first, check if the index is always within the window range k. 
2. then, start your operations. 
3. make sure you keep adding all of the indexes to the queue. 
4. but the key part is, once you reach an index where it was maximum then any others, just remove all of the previous indexes from the deque. 
5. adding values to results array -> only when within range, and 2 conditions:
    1. if the index value gives the max then the others. 
    2. ******if the index value is already out of the scope *******
"""

from collections import deque

nums = [1,-1]
k = 1


q = deque()      # will hold indices
res = []

for i, num in enumerate(nums):
    # 1. Remove indices out of current window
    if q and q[0] <= i - k:
        q.popleft()

    # 2. Remove smaller numbers from the back
    while q and nums[q[-1]] < num:
        q.pop()

    # 3. Add current index
    q.append(i)

    # 4. Append current max (from front)
    if i >= k - 1:
        res.append(nums[q[0]])

    

print(res)