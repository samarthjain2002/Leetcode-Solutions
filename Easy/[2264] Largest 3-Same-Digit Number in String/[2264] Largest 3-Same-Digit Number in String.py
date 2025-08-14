"""
Accepted
2264 [Easy]
Runtime: 0 ms, faster than 100.00% of Java online submissions for Largest 3-Same-Digit Number in String.
Memory Usage: 17.84 MB, less than 39.13% of Java online submissions for Largest 3-Same-Digit Number in String.
"""
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        numStr = str(num)
        res = ""
        for i in range(9, -1, -1):
            if str(i) * 3 in numStr:
                return str(i) * 3
        return res



"""
Runtime: 38 ms, faster than 79.71% of Java online submissions for Largest 3-Same-Digit Number in String.
Memory Usage: 16.25 MB, less than 59.27% of Java online submissions for Largest 3-Same-Digit Number in String.
"""
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        for i in range(0,len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                good = num[i] + num[i+1] + num[i+2]
                if res == "" or int(good) > int(res):
                    res = str(good)

        return res