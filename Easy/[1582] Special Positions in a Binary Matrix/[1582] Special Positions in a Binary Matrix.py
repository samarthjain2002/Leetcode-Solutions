"""
Accepted
1582 [Easy]
Runtime: 171 ms, faster than 21.10% of Python3 online submissions for Special Positions in a Binary Matrix.
Memory Usage: 16.87 MB, less than 14.98% of Python3 online submissions for Special Positions in a Binary Matrix.
"""
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rowSum = []
        for i in range(0,len(mat)):
            sum = 0
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    sum += 1
                if j == len(mat[i]) - 1:
                    rowSum.append(sum)
        
        colSum = []
        for j in range(len(mat[0])):
            sum = 0
            for i in range(len(mat)):
                if mat[i][j] == 1:
                    sum += 1
                if i == len(mat) - 1:
                    colSum.append(sum)
                    
        count = 0
        for i in range(0,len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and rowSum[i] == 1 and colSum[j] == 1:
                    count += 1

        return count