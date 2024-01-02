"""
Accepted
2610 [Medium]
Runtime: 103 ms, faster than 5.01% of Python3 online submissions for Convert an Array Into a 2D Array With Conditions.
Memory Usage: 17.09 MB, less than 23.26% of Python3 online submissions for Convert an Array Into a 2D Array With Conditions.
"""
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        numCount = defaultdict(int)
        res = []
        for num in nums:
            if numCount[num] == len(res):
                res.append([num])
            else:
                res[numCount[num]].append(num)
            numCount[num] += 1

        return res