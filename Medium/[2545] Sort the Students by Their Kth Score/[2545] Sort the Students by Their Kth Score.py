"""
Accepted
2545 [Medium]
Runtime: 321 ms, faster than 75.95% of Python3 online submissions for Sort the Students by Their Kth Score.
Memory Usage: 22.52 MB, less than 78.43% of Python3 online submissions for Sort the Students by Their Kth Score.
"""
class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        def custom_sort_condition(item):
            return -item[k]
        score.sort(key = custom_sort_condition)

        return score