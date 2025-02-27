"""
Accepted
873 [Medium]
Runtime: 793 ms, faster than 74.50% of Python3 online submissions for Length of Longest Fibonacci Subsequence.
Memory Usage: 17.93 MB, less than 80.79% of Python3 online submissions for Length of Longest Fibonacci Subsequence.
"""
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        hashSet = set(arr)

        res = 0
        count = 0
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                first = arr[i]
                second = arr[j]
                count = 2
                while (first + second) in hashSet:
                    count += 1
                    res = max(res, count)
                    first, second = second, first + second
        return res


"""
Runtime: 1146 ms, faster than 41.72% of Python3 online submissions for Length of Longest Fibonacci Subsequence.
Memory Usage:  25.56 MB, less than 26.49% of Python3 online submissions for Length of Longest Fibonacci Subsequence.
"""
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        dp = [[0] * len(arr) for _ in range(len(arr))]
        arr_map = {n: i for i, n in enumerate(arr)}
        res = 0

        for i in reversed(range(len(arr) - 1)):
            for j in reversed(range(i + 1, len(arr))):
                prev, cur = arr[i], arr[j]
                nxt = prev + cur
                length = 2
                if nxt in arr_map:
                    length = 1 + dp[j][arr_map[nxt]]
                    res = max(res, length)
                dp[i][j] = length
        return res