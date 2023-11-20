'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''
def productArrayExceptSelf(nums):
        n = len(nums)

        leftProducts = [1] * n
        rightProducts = [1] * n

        multiplier = 1
        for i in range(1,n):
            multiplier *= nums[i-1]
            leftProducts[i] = multiplier

        multiplier = 1
        for i in range(n-2,-1,-1):
            multiplier *= nums[i+1]
            rightProducts[i] = multiplier

        result = [leftProducts[i] * rightProducts[i] for i in range(n)]
        return result

        print("Origional Array {}\n"
              "Length of Array {}\n"
              "Left Product of Array {}\n"
              "Right Product of Array {}\n"
              "".format(nums,n,leftProducts,rightProducts))
        print("Output should be [24,60,40,30]")

nums = [5,2,3,4]
print(productArrayExceptSelf(nums))
