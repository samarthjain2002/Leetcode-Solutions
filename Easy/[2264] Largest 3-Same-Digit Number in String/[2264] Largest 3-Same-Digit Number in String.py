"""
Accepted
2264 [Easy]
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