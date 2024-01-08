class Solution:
    def solution_method_1(self,nums):
        print(f"Origional Array: {nums}")
        if len(nums) <= 2:
            return len(nums)

        unq = 2
        for i in range(2,len(nums)):
            if nums[i] != nums[unq-2]:
                nums[unq] = nums[i]
                unq += 1
        print(f"Result Array: {nums}")
        return unq

nums = [1,1,1,2,2,3]
nums = [0,0,1,1,1,1,2,3,3]
obj = Solution()
print(f"Method-1: {obj.solution_method_1(nums)}")