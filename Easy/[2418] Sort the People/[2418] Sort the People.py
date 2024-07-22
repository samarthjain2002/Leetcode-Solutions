"""
Accepted
2418 [Easy]
Runtime: 110 ms, faster than 39.76% of Python3 online submissions for Sort the People.
Memory Usage:  17.11 MB, less than 14.55% of Python3 online submissions for Sort the People.
"""
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashMap = {}
        for i, height in enumerate(heights):
            hashMap[height] = names[i]

        heights.sort()
        heights.reverse()

        return [hashMap[height] for height in heights]