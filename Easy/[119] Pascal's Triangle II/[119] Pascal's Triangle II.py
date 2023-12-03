"""
Accepted
119 [Easy]
Runtime: 13 ms, faster than 65.27% of Python online submissions for Pascal's Triangle II.
Memory Usage: 13.17 MB, less than 75.82% of Python online submissions for Pascal's Triangle II.
"""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        tri=[]

        for i in range(0,rowIndex+1):
            tri.append([])
            for j in range(0,i+1):
                tri[i].append(1)

        for i in range(0,len(tri)):
            for j in range(0,len(tri[i])):
                if j==0 or i==j:
                    pass
                else:
                    tri[i][j]=tri[i-1][j-1]+tri[i-1][j]

        return tri[rowIndex]