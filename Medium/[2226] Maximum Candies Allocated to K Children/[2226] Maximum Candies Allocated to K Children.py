"""
Accepted
2226 [Medium]
Runtime: 119 ms, faster than 99.13% of Python3 online submissions for Maximum Candies Allocated to K Children.
Memory Usage: 29.83 MB, less than 18.92% of Python3 online submissions for Maximum Candies Allocated to K Children.
"""
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0

        low, high = 1, sum(candies) // k
        res = 0
        while low <= high:
            mid = low + ((high - low) // 2)

            count = 0
            for candy in candies:
                count += candy // mid

            if count >= k:
                res = mid
                low = mid + 1
            else:
                high = mid - 1

        return res