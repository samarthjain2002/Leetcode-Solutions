"""
Accepted
3849 [Medium]
Runtime: 317 ms, faster than 60.98% of Python3 online submissions for Maximum Bitwise XOR After Rearrangement.
Memory Usage: 22.12 MB less than 97.75% of Python3 online submissions for Maximum Bitwise XOR After Rearrangement.
"""
class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        o = t.count('1')
        z = len(s) - o
        res = ""
        for bit in s:
            if bit == '1' and z:
                res += '1'
                z -= 1
            elif bit == '0' and o:
                res += '1'
                o -= 1
            else:
                res += '0'
        return res