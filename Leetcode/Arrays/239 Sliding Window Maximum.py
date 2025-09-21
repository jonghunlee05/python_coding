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
 
 
the key is with indexing!!!!
to solve this, we need much more efficient than max scanning and popleft method. 


when you observe carefully, given n len of array, and k, 

the elements that max will have is \
    
n = 8, k = 3 -> 6 slides. cuz 8 -3 + 1
n = 8, k = 4 -> 5 slides cuz 8 - 4 + 1. the "1" is the first chucnk being observed.


so, much more efficient looping is possible. 

for n - k + 1 loops -> 

1. get the max value for projections of first k elements. 
2. use k to not iterate, but slicing directly. 
3. if the max is not greater then the last max, add the last max again. 

"""


nums = [1,3,-1,-3,5,3,6,7]
k = 3

max_nums = []
max_idx = 0



for i in range(len(nums) - k + 1): # iterate for n - k + 1 times
    
    # check if max_idx is still on the range. 
   

    max_nums.append(max(nums[i:i+k]))
    
    
print(max_nums)
