def triletsSum(nums):
    print(nums)
    nums.sort()
    print(nums)
    resultTriplet = set()
    left = 0
    right = len(nums) -1
    print("Left:{},Right:{}".format(left,right))
    for i in range(len(nums) - 1):
        left = i + 1
        right = len(nums) -1

        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            print("Sum of {} + {} + {} = {}".format(nums[i],nums[left],nums[right],sum))

            if sum == 0:
                resultTriplet.add((nums[i],nums[left],nums[right]))
            if sum < 0:
                left+=1
            else:
                right-=1
    return list(resultTriplet)


nums = [1, -2, 1, 0, 5]
nums = [-1,0,1,2,-1,-4]
print(triletsSum(nums))
