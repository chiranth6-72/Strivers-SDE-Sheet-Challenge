
#   ***  Program to generate Pascal’s Triangle
# Problem Statement: This problem has 3 variations. They are stated below:

# Variation 1: Given row number r and column number c. Print the element at position (r, c) in Pascal’s triangle.

# Variation 2: Given the row number n. Print the n-th row of Pascal’s triangle.

# Variation 3: Given the number of rows n. Print the first n rows of Pascal’s triangle.




# Variation 3: Naive Approach O(n^3)

class Solution:
    def nCr(self, n, r):
        res = 1
        for i in range(r):
            res = res * (n-i)
            res = res // (i+1)
        return int(res)


    def generate(self, numRows: int) -> List[List[int]]:
        ans = []

        for row in range(1, numRows+1):
            temp = []
            for col in range(1, row+1):
                temp.append(self.nCr(row-1, col-1))
            ans.append(temp)
        return ans
    
# Variation 3: Optimal Approach O(n^2)


def generateRow(row):
    ans = 1
    ansRow = [1]

    for col in range(1, row):
        ans *= (row-col)
        ans //= col
        ansRow.append(ans)
    return ansRow

def printPascal(n:int):
    # Write your code here.
    # Return a list of lists.
    ans = []

    for row in range(1, n+1):
        ans.append(generateRow(row))
    return ans
    