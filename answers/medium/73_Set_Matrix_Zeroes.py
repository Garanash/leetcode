class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        sp_columns = []
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            flag = False
            for j in range(m):
                if matrix[i][j] == 0:
                    sp_columns.append(j)
                    flag = True
                    x = j
                    while x >= 0:
                        matrix[i][x] = 0
                        x -= 1
                    c = i
                    while c >= 0:
                        matrix[c][j] = 0
                        c -= 1
                elif j in sp_columns:
                    if matrix[i][j] == 0:
                        flag = True
                    matrix[i][j] = 0
                if flag:
                    matrix[i][j] = 0


