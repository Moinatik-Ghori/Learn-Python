'''
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
'''
class Solution:
    def search_insert_position(self,arr,target):
        print(f"Array:{arr}\nTarget:{target}")
        for ind,val in enumerate(arr):
            if target <= val:
                return ind
        return ind + 1



arr = [1,3,5,6]
target = 7

b1=Solution()
print(f"Insert position should be {b1.search_insert_position(arr,target)}")
