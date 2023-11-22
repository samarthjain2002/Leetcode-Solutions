"""
Accepted
1424 [Medium]
Runtime: 855 ms, faster than 14.41% of Python3 online submissions for Diagonal Traverse II.
Memory Usage: 47.31 MB, less than 7.35% of Python3 online submissions for Diagonal Traverse II.
"""
#https://chat.openai.com/share/dcc22d70-75b3-4929-8ae7-d90175e72fd1
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        sum = []
        for i, sublist in enumerate(nums):
            for j, value in enumerate(sublist):
                sum.append([value, i+j, i])

        def custom_sort_condition(item):
            return (item[1], -item[2])
        sum.sort(key=custom_sort_condition)

        res = []
        for i in sum:
            res.append(i[0])

        return res