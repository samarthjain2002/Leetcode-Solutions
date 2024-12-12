"""
Accepted
74 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Search a 2D Matrix.
Memory Usage: 17.60 MB, less than 16.32% of Python3 online submissions for Search a 2D Matrix.
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])

        def search_first_col():
            top, bottom = 0, M - 1
            
            if matrix[top][0] > target:
                return False
            if matrix[bottom][0] <= target:
                return bottom
            
            while top != bottom - 1:
                mid = top + ((bottom - top) // 2)
                if matrix[mid][0] <= target:
                    top = mid
                elif matrix[mid][0] > target:
                    bottom = mid
            return top


        def search_row(row):
            left, right = 0, N - 1
            while left <= right:
                mid = left + ((right - left) // 2)
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return False

        
        row = search_first_col()
        return search_row(row)