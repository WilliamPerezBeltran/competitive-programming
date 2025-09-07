import unittest

"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

def twoSum(nums, target):
    my_dict = dict()
    for index, value in enumerate(nums):
        comparo = target - value
        if comparo in my_dict: 
            return [index, my_dict[comparo]]
            return [my_dict[comparo], index]
        else:
            my_dict[value] = index
    return None 

class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(twoSum([2, 7, 11, 15], 9),[1, 0])  
        self.assertEqual(twoSum([3, 2, 4], 6),[2, 1])  
        self.assertEqual(twoSum([3, 3], 6),[1, 0])  
        self.assertEqual(twoSum([1, 5, 7, -1, 5], 6),[1, 0])  
        self.assertEqual(twoSum([0, 4, 3, 0], 0),[3, 0])  
        self.assertEqual(twoSum([1, 2, 3, 4, 5], 10),None )  

if __name__ == "__main__":
    unittest.main()
# Ejemplo 1
