def findMedian(arr):
    print(arr)
    arr.sort()
    print(arr)
    n = len(arr)
    print(f"Total Length : {n}")
    mid_ind = n // 2
    return arr[n // 2]

arr = [0,1,2,4,6,5,3]
print(f"Median is : {findMedian(arr)}")
