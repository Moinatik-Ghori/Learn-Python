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

arr = [2,7,11,15]
target = 9
twosumSolution(arr,target)
