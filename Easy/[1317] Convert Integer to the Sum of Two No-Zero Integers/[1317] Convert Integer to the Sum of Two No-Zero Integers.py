"""
Accepted
1317 [Easy]
Runtime: 97 ms, faster than 39.02% of Python3 online submissions for Convert Integer to the Sum of Two No-Zero Integers.
Memory Usage: 17.75 MB, less than 52.92% of Python3 online submissions for Convert Integer to the Sum of Two No-Zero Integers.
"""
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for num in range(1, n):
            if str(num).count('0') == 0 and str(n - num).count('0') == 0:
                return [num, n - num]