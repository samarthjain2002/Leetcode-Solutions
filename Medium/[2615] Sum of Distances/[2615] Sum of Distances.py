"""
Accepted
2615 [Medium]
Runtime: 133 ms, faster than 65.75% of Python3 online submissions for Sum of Distances.
Memory Usage: 55.44 MB, less than 50.79% of Python3 online submissions for Sum of Distances.
"""
# Grouping + PrefixSum Solution
# TC: O(n), SC: O(n)
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        groups = defaultdict(list)
        for i, num in enumerate(nums):
            groups[num].append(i)

        res = [0] * len(nums)
        for group in groups.items():
            num, arr = group

            total = sum(arr)
            prefix_total = 0
            for i, idx in enumerate(arr):
                res[idx] = ((idx * i) - prefix_total) + ((total - (prefix_total + idx)) - ((len(arr) - 1 - i) * idx))
                prefix_total += idx
                
        return res