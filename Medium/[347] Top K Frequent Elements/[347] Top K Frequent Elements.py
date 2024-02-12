"""
Accepted
347 [Medium]
Runtime: 75 ms, faster than 98.89% of Python3 online submissions for Top K Frequent Elements.
Memory Usage:  21.26 MB, less than 70.66% of Python3 online submissions for Top K Frequent Elements.
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ele = [[c, n] for n, c in Counter(nums).items()]
        ele.sort()
        ele.reverse()
        return [number for frequency, number in ele[:k]]