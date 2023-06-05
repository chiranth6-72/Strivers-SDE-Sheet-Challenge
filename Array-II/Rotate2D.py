
#   *** Rotate Image by 90 degree
# Problem Statement: Given a matrix, your task is to rotate the matrix 90 degrees clockwise.


# Brute Approach

from copy import deepcopy
def rotate(matrix):
    n = len(matrix)
    temp = [[None for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            temp[j][n-1-i] = matrix[i][j]
            
    matrix = deepcopy(temp)
    print(matrix)
    
    
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotate(matrix)


# Optimal Approach
# 1. Transpose the matrix --> 2. Reverse each row

def rev(arr, l, r):
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

def rotate2D(matrix):
    n = len(matrix)
    
    # Transpose
    for i in range(n-1):
        for j in range(i+1, n):
            if i != j: 
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse
    
    for i in range(n):
        matrix[i].reverse()
        
    print(matrix) 
    
rotate2D(matrix)