class Solution:
    def find_smallest_greater_than_target(self,letters,target):
        for char in letters:
            if char > target:
                print(f"Target:{target} Char:{char}")
                return char
        return letters[0]

obj = Solution()
s = ["c" , "f" , "j"]
target = "a"
print(f"{obj.find_smallest_greater_than_target(s,target)}")