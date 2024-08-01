"""
Accepted
2678 [Easy]
Runtime: 51 ms, faster than 25.42% of Python3 online submissions for Number of Senior Citizens.
Memory Usage: 16.58 MB, less than 32.17% of Python3 online submissions for Number of Senior Citizens.
"""
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for  detail in details:
            if int(detail[11: 13]) > 60:
                count += 1
        return count