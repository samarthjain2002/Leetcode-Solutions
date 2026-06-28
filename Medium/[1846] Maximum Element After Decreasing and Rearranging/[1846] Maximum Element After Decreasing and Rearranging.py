"""
Accepted
1846 [Medium]
Runtime: 27 ms, faster than 64.54% of Python3 online submissions for Maximum Element After Decreasing and Rearranging.
Memory Usage: 28.28 MB, less than 56.03% of Python3 online submissions for Maximum Element After Decreasing and Rearranging.
"""
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()

        cur = 0
        for i, num in enumerate(arr):
            if num >= cur + 1:
                arr[i] = cur + 1
                cur += 1
        return arr[-1]