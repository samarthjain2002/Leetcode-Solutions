"""
Accepted
2948 [Medium]
Runtime: 227 ms, faster than 94.44% of Python3 online submissions for Make Lexicographically Smallest Array by Swapping Elements.
Memory Usage: 95.77 MB, less than 5.56% of Python3 online submissions for Make Lexicographically Smallest Array by Swapping Elements.
"""
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups = []
        num_to_group = {}

        for num in sorted(nums):
            if not groups or abs(groups[-1][-1] - num) > limit:
                groups.append(deque())
            groups[-1].append(num)
            num_to_group[num] = len(groups) - 1

        res = []
        for num in nums:
            j = num_to_group[num]
            res.append(groups[j].popleft())
        return res