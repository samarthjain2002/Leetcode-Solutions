"""
Accepted
66 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Plus One.
Memory Usage: 17.73 MB, less than 49.65% of Python3 online submissions for Plus One.
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = [0] + digits

        carry = True
        for i in range(len(res) - 1, -1, -1):
            if carry:
                if res[i] == 9:
                    res[i] = 0
                else:
                    res[i] += 1
                    break
        return res if res[0] == 1 else res[1 : ]