"""
Accepted
2698 [Medium]
Runtime: 1196 ms, faster than 35.72% of Python3 online submissions for Find the Punishment Number of an Integer.
Memory Usage: 17.92 MB, less than 40.18% of Python3 online submissions for Find the Punishment Number of an Integer.
"""
class Solution:
    def punishmentNumber(self, n: int) -> int:
        res = 0

        def partition(i, cur, target, string):
            if i == len(string) and cur == target:
                return True

            for j in range(i, len(string)):
                if partition(j + 1, cur + int(string[i : j + 1]), target, string):
                    return True
            return False

        for i in range(1, n + 1):
            if partition(0, 0, i, str(i**2)):
                res += i**2
        return res