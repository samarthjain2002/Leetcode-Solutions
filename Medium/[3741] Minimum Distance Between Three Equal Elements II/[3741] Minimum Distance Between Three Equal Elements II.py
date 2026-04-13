"""
Accepted
3741 [Medium]
Runtime: 324 ms, faster than 70.59% of Python3 online submissions for Minimum Distance Between Three Equal Elements II.
Memory Usage: 50.86 MB less than 36.90% of Python3 online submissions for Minimum Distance Between Three Equal Elements II.
"""
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        hashMap = defaultdict(list)
        for i, num in enumerate(nums):
            hashMap[num].append(i)

        res = float("inf")
        for num in hashMap:
            if len(hashMap[num]) >= 3:
                for i in range(2, len(hashMap[num])):
                    res = min(res, 2 * (hashMap[num][i] - hashMap[num][i - 2]))
        return res if res < float("inf") else -1