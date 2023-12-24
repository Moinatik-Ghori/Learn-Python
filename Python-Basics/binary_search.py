'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''
class Solution:
    def binary_search(self,arr,target):
        n = len(arr)
        print(f"Array is : {arr}\nlength:{n}\nTarget is {target}")

        left = 0
        right = n - 1
        while left <= right:
            print(f"Left:{left} Right:{right}")
            if arr[0] > target:
                return -1
            elif target == arr[left]:
                return left
            elif target == arr[right]:
                return right
            elif target > arr[left]:
                left += 1
            elif target < arr[right]:
                right -= 1
            else:
                return -1
        return -1



b1 = Solution()
arr = [5]
target = 5
print(f"Index Position is : {b1.binary_search(arr,target)}")


