"""
Accepted
1945 [Easy]
Runtime: 28 ms, faster than 96.97% of Python3 online submissions for Sum of Digits of String After Convert.
Memory Usage: 16.56 MB, less than 37.00% of Python3 online submissions for Sum of Digits of String After Convert.
"""
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        convert = ""
        for char in s:
            convert += str(ord(char) - ord('a') + 1)
        transform = 0
        for i in range(k):
            transform = 0
            for dig in convert:
                transform += int(dig)
            convert = str(transform)
        return transform