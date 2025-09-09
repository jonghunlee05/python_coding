"""
Example LeetCode Solution Template

Problem: Two Sum
Difficulty: Easy
URL: https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
"""

def two_sum(nums, target):
    """
    Find two numbers in nums that add up to target.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List of two indices
    """
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = two_sum(nums1, target1)
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {result1}")
    print(f"Explanation: nums[{result1[0]}] + nums[{result1[1]}] = {nums1[result1[0]]} + {nums1[result1[1]]} = {target1}")
    print()
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = two_sum(nums2, target2)
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {result2}")
    print()
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    result3 = two_sum(nums3, target3)
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {result3}")
