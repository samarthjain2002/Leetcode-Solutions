"""
Accepted
957 [Medium]
Runtime: 39 ms, faster than 75.50% of Python3 online submissions for Prison Cells After N Days.
Memory Usage:  16.54 MB, less than 75.50% of Python3 online submissions for Prison Cells After N Days.
"""
class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        def next_day(cells: List[int]) -> List[int]:
            return [0] + [int(cells[i - 1] == cells[i + 1]) for i in range(1, 7)] + [0]
        
        seen = {}
        
        while n > 0:
            cell_tuple = tuple(cells)
            if cell_tuple in seen:
                cycle_length = seen[cell_tuple] - n
                n %= cycle_length
            seen[cell_tuple] = n
            
            if n > 0:
                n -= 1
                cells = next_day(cells)
        
        return cells