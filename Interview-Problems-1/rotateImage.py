"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

"""
def rotateImage(matrix):
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix[0])):
            print("First")
            print("iteration {}, {} and value {}".format(i,j,matrix[i][j]))
            print("iteration {}, {} and value {}".format(j,i,matrix[j][i]))
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            print("Second")
            print("iteration {}, {} and value {}".format(i,j,matrix[i][j]))
            print("iteration {}, {} and value {}".format(j,i,matrix[j][i]))

    for row in matrix:
        print("before",row)
        row.reverse()
        print("After",row)

    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotateImage(matrix))
