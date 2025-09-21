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
 
 
using deque, popleft instead of manually moving the array, 
can just have simple for loop. 


1. we get the first k elements in the nums list. 
2. find the max, save it to the max_nums list. 
3. breaking condition is, if the length of the nums list is less than k. 
4. return max_nums list. 

"""

from collections import deque
nums = [1]
k = 1

nums = deque(nums)

max_nums = []


while len(nums) >= k:
    
    temp_set = set()
    
    for i in range(k): # add the elements to the temp list, find max and add to max_nums
        temp_set.add(nums[i])
    
    max_nums.append(max(temp_set)) # added to max_nums.
    nums.popleft() # remove the first element.


print(max_nums)