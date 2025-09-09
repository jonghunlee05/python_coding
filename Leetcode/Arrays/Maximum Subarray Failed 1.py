"""

Why it failed?

Cuz i was just so fixated on the for i in range method... 

instead, i could have just directly accessed the for i in array. 


"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        idx = [] # only contains positive numbers
        norm_sum = 0
        max_sum = 0
        for i in range(0, len(nums)):
            if nums[i] > 0:
                idx.append(i)

        if len(idx) == 0: return max(nums)
                
        
        for i in range(0, len(idx)): # only gets the positive ones
            norm_sum = 0 #resetting.
            for j in range(idx[i], len(nums)):
                norm_sum += nums[j]
                if norm_sum > max_sum:
                    max_sum = norm_sum
                    
                
        return max_sum
    
    
    
    