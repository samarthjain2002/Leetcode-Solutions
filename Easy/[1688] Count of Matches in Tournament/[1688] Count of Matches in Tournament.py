"""
Accepted
1688 [Easy]
Runtime: 37 ms, faster than 59.83% of Python3 online submissions for Count of Matches in Tournament.
Memory Usage: 16.22 MB, less than 35.39% of Python3 online submissions for Count of Matches in Tournament.
"""
class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n > 1:
            matches += int(n / 2)
            if n % 2 == 0:
                n = int(n / 2)
            else:
                n = int(n / 2) + 1

        return matches
    

"""
Accepted
1688 [Easy]
Runtime: 45 ms, faster than 9.48% of Python3 online submissions for Count of Matches in Tournament.
Memory Usage: 16.41 MB, less than 5.91% of Python3 online submissions for Count of Matches in Tournament.
"""
class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n - 1