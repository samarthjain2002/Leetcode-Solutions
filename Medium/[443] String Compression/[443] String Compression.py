"""
Accepted
443 [Medium]
Runtime: 76 ms, faster than 5.98% of Python3 online submissions for String Compression.
Memory Usage:  16.57 MB, less than 86.57% of Python3 online submissions for String Compression.
"""
class Solution:
    def compress(self, chars: List[str]) -> int:
        N = len(chars)
        res = ""
        i = 0
        while i < N:
            curEle = chars[i]
            count = 0
            while i < N and chars[i] == curEle:
                count += 1
                i += 1
            if count > 1:
                res += curEle + str(count)
            else:
                res += curEle
                
        for i in range(len(res)):
            chars[i] = list(res)[i]
        return len(chars[:len(res)])