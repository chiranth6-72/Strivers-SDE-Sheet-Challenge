
#   ***  Set Matrix Zero
# Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.


# Brute Approach

def markRow(mat, n, m, i):
    for j in range(m):
        if mat[i][j] != 0:
            mat[i][j] = -1
            
def markCol(mat, n, m, j):
    for i in range(n):
        if mat[i][j] != 0:
            mat[i][j] = -1
            
def zeroMat(mat, n, m):
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                markRow(mat, n, m, i)
                markCol(mat, n, m, j)
                
    for i in range(n):
        for j in range(m):
            if mat[i][j] == -1:
                mat[i][j] = 0
                
    return mat


if __name__ == "__main__":
	matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
	n = len(matrix)
	m = len(matrix[0])
	ans = zeroMat(matrix, n, m)

	print("The Final matrix is:")
	for row in ans:
	    for ele in row:
	        print(ele, end=" ")
	    print()
     
     
# Optimal Approach


# Intuition:
# In the previous approach, the time complexity is minimal as the traversal of a matrix takes at least O(N*M)(where N = row and M = column). In this approach, we can just improve the space complexity. So, instead of using two extra matrices row and col, we will use the 1st row and 1st column of the given matrix to keep a track of the cells that need to be marked with 0. But here comes a problem. If we try to use the 1st row and 1st column to serve the purpose, the cell matrix[0][0] is taken twice. To solve this problem we will take an extra variable col0 initialized with 1. Now the entire 1st row of the matrix will serve the purpose of the row array. And the 1st column from (0,1) to (0,m-1) with the col0 variable will serve the purpose of the col array.

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        col0 = None
        
        # *** Tracking
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0
        # *** Setting
        
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # *** Edge Case       

        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0

        if col0 == 0:
            for i in range(n):
                matrix[i][0] = 0