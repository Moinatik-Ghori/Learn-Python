def calLength(heightArray):
    print(heightArray)
    leftPointer = 0
    rightPointer = len(heightArray) - 1
    width = 0
    maxWater = 0
    while leftPointer < rightPointer:
        leftHeight = heightArray[leftPointer]
        rightHeight = heightArray[rightPointer]
        width = rightPointer - leftPointer
        minHeight =  min(leftHeight,rightHeight)
        maxWater = max(maxWater, width * minHeight)
        print("Left Pointer {} Right Pointer {} Width {} Left Height {} Right Height {} Min Height {} Max Water {}".format(leftPointer,rightPointer,width,leftHeight,rightHeight,minHeight,maxWater))
        if leftHeight < rightHeight:
            leftPointer += 1
        else:
            rightPointer -= 1
    return maxWater


height = [1,8,6,2,5,4,8,3,7]
height = [2,3,4,5,18,17,6]
calLength(height)
