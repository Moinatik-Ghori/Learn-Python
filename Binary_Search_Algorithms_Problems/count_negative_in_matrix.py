'''
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

Example 1:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:
Input: grid = [[3,2],[1,0]]
Output: 0
'''
class Solution:
    def find_negative_number(self,mat):
        print(f"Matrix : {mat}")
        rows = len(mat)
        cols = len(mat[0])
        total_element = rows * cols
        total_neg = 0
        for row in range(rows-1,-1,-1):
            print(f"Row:{row}")
            for col in range(cols-1,-1,-1):
                print(f"Cols:{col} , Mat:{mat[row][col]}")
                if mat[row][col] >= 0:
                    print("Break the loop")
                    break
                else:
                    total_neg += 1
        return total_neg



grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
b1 = Solution()
print(f"Negative count is {b1.find_negative_number(grid)}")