"""
Accepted
1441 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Build an Array With Stack Operations.
Memory Usage: 19.25 MB, less than 65.11% of Python3 online submissions for Build an Array With Stack Operations.
"""
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        cur = 0
        for num in target:
            for _ in range(num - cur - 1):
                res.append("Push")
                res.append("Pop")
            res.append("Push")
            cur = num
        return res