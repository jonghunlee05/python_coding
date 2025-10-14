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


but what we have to do is, don't change the nums. 
make a deque that has k length. 

1. just keep the index until max appears. 
2. once max appears, unless the next max appears or index out of range, 
keep adding the new indexs to the queue. 
3. once new max appears, pop all of the queue and put the new max_idx only. 
4. so, let the first element in the queue be the max. 
"""

from collections import deque

nums = [1,-1]
k = 1

q = deque([0])
max_nums = []


for i in range(len(nums)):
    
    if len(q) == k: 
        q.clear()
        q.append(i)
        print(q)
    
    if i + 1 < k or nums[i] > nums[q[0]]: # new max occured!
        q.clear()
        q.append(i)
        print(q)
    else: 
        q.append(i)
        print(q)
    
    if i + 1 >= k: 
        max_nums.append(nums[q[0]])
    

print(max_nums)