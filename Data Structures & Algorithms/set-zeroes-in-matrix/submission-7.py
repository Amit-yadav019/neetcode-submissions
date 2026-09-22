
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r = len(matrix)
        c = len(matrix[0])
        rowTrack = [0] * r
        colTrack = [0] * c
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0 :
                    rowTrack[i] = -1 
                    colTrack[j] = -1 
        for i in range(r):
            for j in range(c):
                if rowTrack[i] == -1 or colTrack[j] == -1 :
                    matrix[i][j] = 0             
        
        