"""
Accepted
38 [Medium]
Runtime: 5 ms, faster than 82.73% of Python3 online submissions for Count and Say.
Memory Usage: 18.07 MB, less than 20.58% of Python3 online submissions for Count and Say.
"""
class Solution:
    def countAndSay(self, n: int) -> str:
        enc = "1z"

        for _ in range(n - 1):
            newEnc = ""
            num = enc[0]
            count = 1
            for i in range(1, len(enc)):
                if enc[i] != num:
                    newEnc += str(count) + num
                    num = enc[i]
                    count = 1
                else:
                    count += 1
            enc = newEnc + 'z'
        
        return enc[ : -1]