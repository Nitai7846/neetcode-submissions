class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]
        
        
        def reverse(row):
            row_n = len(row)
            for i in range(row_n//2):
                row[i], row[row_n-i-1] = row[row_n-i-1], row[i]
            return row 
        
        for i in range(0 ,n):
            row = reverse(matrix[i])
        
        