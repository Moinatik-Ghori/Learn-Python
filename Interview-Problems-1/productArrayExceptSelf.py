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
