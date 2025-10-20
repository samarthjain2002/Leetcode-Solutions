"""
Accepted
2011 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Final Value of Variable After Performing Operations.
Memory Usage: 17.62 MB, less than 89.00% of Python3 online submissions for Final Value of Variable After Performing Operations.
"""
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for op in operations:
            if op[1] == '-':
                res -= 1
            else:
                res += 1
        return res