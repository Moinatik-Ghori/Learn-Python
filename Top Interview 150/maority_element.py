'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109


Follow-up: Could you solve the problem in linear time and in O(1) space?
'''
class Solution:
    def solution_method_1(self,nums):
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        print(nums)
        curr_element,unq = 0,0
        count = 1
        result_dict = {}
        for i in range(1,len(nums)):
            if nums[unq] == nums[i]:
                count += 1
                unq += 1
                result_dict[nums[i]] = count
                print(f"Index:{i}, Element:{nums[i]} , Dictionary : {result_dict}")
            else:
                print(f"Index:{i}, Element:{nums[i]} , Dictionary : {result_dict}")
                count = 1
                unq += 1
                result_dict[nums[i]] = count
        print(f"Final Dictionary :{result_dict}")
        max_element = max(result_dict, key=result_dict.get)
        print(f"Max Element:{max_element}")
        return max_element


nums = [1,1,2,2,1,1,1,2,2,3,2,2,3,3,3]
nums = [1]
obj = Solution()
print(f"Method-1: {obj.solution_method_1(nums)}")
