def twosumSolution(arr,target):
    # Take index dictionary for storing the input array value and its position
    indexDict = {}
    result = []
    for ind, value in enumerate(arr):
        reminder = target - value
        if reminder in indexDict:
            result.append([indexDict[reminder],ind])
        indexDict[value] = ind
    print(result)

arr = [4, 6, 12, 14, 1, 9]
target = 14
twosumSolution(arr,target)
