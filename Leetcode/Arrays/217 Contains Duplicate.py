"""

the key point is, set is allergic to duplicates. 

we can make a new set. 
Then, add the elements from the existing set. 

Every time, we check if the element is already in the exisiting set. 

finally, check the lenght of the existing vs new set. 



"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        s = set()
        
        for i in nums:
            s.add(i)
        

        return len(s) != len(nums)
