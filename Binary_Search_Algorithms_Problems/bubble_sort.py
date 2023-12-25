class Solution:
    def bubble_sort_method_1(self,nums):
        print(nums)
        has_swapped = True
        while has_swapped:
            has_swapped = False
            for i in range(len(nums) - 1):
                print(f"Iteration-{i}, {has_swapped}")
                if nums[i] > nums[i+1]:
                    nums[i],nums[i+1] = nums[i+1],nums[i]
                    print(f"List: {nums}")
                    has_swapped = True
        print(nums)

l1 = Solution()

nums = [8,4,10,7,2,5,9,1,3,6,2]
l1.bubble_sort_method_1(nums)
