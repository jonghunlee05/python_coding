"""

Just get the counter, then find the max on that. 

remember, counter is a dictionary that counts the frequency of each element.

"""

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_c = Counter(nums)
        return max(nums_c, key=nums_c.get)

