"""
Why this works? 

Cuz instead of focusing on each element index, 
I just focused on get the element directly. 

Also,it's from something called Kadane's algorithm.

Just think of it like -> ok the current indiivdual number is bigger? just bin the previous guys. 
I was just so fixated on the starting index, ending index...
Next time i should just make it simple.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        current_sum = nums[0]
        max_sum = nums[0]

        for i in nums[1:]:
            current_sum = max(i, current_sum + i)
            max_sum = max(current_sum, max_sum)


        return max_sum