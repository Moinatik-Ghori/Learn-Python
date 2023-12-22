'''
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Example
arr=[1,3,5,7,9]
The minimum sum is  and the maximum sum is . The function prints
16 24

Sample Input
1 2 3 4 5
Sample Output
10 14
'''
def min_max(arr):
    min_num = min(arr)
    max_num = max(arr)
    sum = 0
    for digit in arr:
        sum += digit
    print((sum-max_num), (sum - min_num))

arr = [1,3,5,7,9]
min_max(arr)
