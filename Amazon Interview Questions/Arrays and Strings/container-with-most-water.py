'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''
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
