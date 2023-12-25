'''
Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
'''
class Solution:
    def find_first_last_position(self,nums,target):
        position = set()
        min_val , max_val = 0,0
        def recurssive(l ,r):
            for ind, digit in enumerate(nums[l:r]):
                print(f"Index:{ind}-->Val:{digit}" )
                if target == digit:
                    print(f"Target:{target} Matched Index:{ind}")
                    position.add(l+ind)
            return position
        print(f"Given Array:{nums} and Target:{target}")
        left , right = 0 , len(nums)
        mid_ind = int((left + right) / 2)
        print(f"Left:{left} Right:{right} Mid_Index:{mid_ind}")
        print(f"Array from {left} to {mid_ind} position : {nums[left:mid_ind]}")
        print(f"Array from {mid_ind} to {right} position : {nums[mid_ind:right]}")
        if target in nums[left:mid_ind]:
            print("First Half")
            position = recurssive(left,mid_ind)
        if target in nums[mid_ind:right]:
            print("Second Half")
            position = recurssive(mid_ind, right)


        if not position:
            return [-1,-1]
        else:
            min_val = min(position)
            max_val = max(position)

        return [min_val,max_val]


nums = [5,7,7,8,8,10]
target = 8
b1 = Solution()
print(f"Position is : {b1.find_first_last_position(nums,target)}")