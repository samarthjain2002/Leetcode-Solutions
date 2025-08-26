"""
Accepted
3000 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Maximum Area of Longest Diagonal Rectangle.
Memory Usage: 17.68 MB, less than 89.78% of Python3 online submissions for Maximum Area of Longest Diagonal Rectangle.
"""
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        diag = 0
        area = 0
        for length, width in dimensions:
            if math.sqrt(length**2 + width**2) > diag:
                diag = math.sqrt(length**2 + width**2)
                area = length * width
            elif math.sqrt(length**2 + width**2) == diag:
                area = max(area, length * width)
        return area