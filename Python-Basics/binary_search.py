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


