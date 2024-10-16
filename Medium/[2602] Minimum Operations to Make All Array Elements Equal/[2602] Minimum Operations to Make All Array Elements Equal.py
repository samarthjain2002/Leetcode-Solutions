"""
Accepted
2602 [Medium]
Runtime: 932 ms, faster than 19.98% of Python3 online submissions for Minimum Operations to Make All Array Elements Equal.
Memory Usage: 44.10 MB, less than 53.47% of Python3 online submissions for Minimum Operations to Make All Array Elements Equal.
"""
class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        N = len(nums)
        nums.sort()
        prefixSums = [0] * N
        prefixSums[-1] = nums[-1]
        for i in range(N - 2, -1, -1):
            prefixSums[i] = prefixSums[i + 1] + nums[i]

        def binarySearch(key):
            low, high = 0, N - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == key:
                    return mid
                elif nums[mid] > key:
                    high = mid - 1
                else:
                    low = mid + 1
            return low

        res = []
        for query in queries:
            pos = binarySearch(query)
            operations = 0

            # Elements less than the query
            if pos != 0:
                if pos < N:
                    operations += (query * pos) - (prefixSums[0] - prefixSums[pos])
                else:
                    operations += (query * pos) - prefixSums[0]

            # Elements greater than the query
            if pos < N:
                operations += prefixSums[pos] - (query * (N - pos))
            
            res.append(operations)
        return res