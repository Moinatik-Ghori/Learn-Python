'''
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
Print the decimal value of each fraction on a new line with  places after the decimal.
Note: This challenge introduces precision problems.
The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

proportion of positive values
proportion of negative values
proportion of zeros
Sample Input

STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]
Sample Output
0.500000
0.333333
0.166667

'''
def plus_minus(arr):
    print("Hello Plus-Minus Program")
    print(f"Array is {arr}")
    n = len(arr)
    pos_cnt, neg_cnt, zero_cnt = 0,0,0
    pos_rto, neg_rto, zero_rto = 0,0,0
    for digit in arr:
        if digit > 0:
            pos_cnt += 1
        elif digit < 0:
            neg_cnt += 1
        else:
            zero_cnt += 1

    print(round(pos_cnt / n,6))
    print(round(neg_cnt / n,6))
    print(round(zero_cnt / n,6))

arr = [-4, 3, -9, 0, 4, 1]

plus_minus(arr)
