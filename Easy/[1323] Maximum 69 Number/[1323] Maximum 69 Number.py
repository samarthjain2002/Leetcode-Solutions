"""
Accepted
1323 [Easy]
Runtime: 97 ms, faster than 39.02% of Python3 online submissions for Maximum 69 Number.
Memory Usage: 17.78 MB, less than 47.05% of Python3 online submissions for Maximum 69 Number.
"""
class Solution:
    def maximum69Number (self, num: int) -> int:
        res = ""
        changed = False
        for dig in str(num):
            if dig == '6' and not changed:
                res += '9'
                changed = True
            else:
                res += dig

        return int(res)