"""
Accepted
3655 [Hard]
Runtime: 6856 ms, faster than 16.89% of Python3 online submissions for XOR After Range Multiplication Queries II.
Memory Usage: 70.38 MB, less than 56.40% of Python3 online submissions for XOR After Range Multiplication Queries II.
"""
TC: O(B*(Q + n)), SC: O(Q + n)
class Solution:
    # Binary Exponentiation
    def power(self, a, b):
        MOD = 10**9 + 7

        if b == 0:
            return 1

        half = self.power(a, b // 2)
        res = (half * half) % MOD

        if b % 2 == 1:
            res = (res * a) % MOD

        return res

    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        B = ceil(sqrt(n))
        MOD = 10**9 + 7

        smallKMap = defaultdict(list)

        for q in queries:
            l, r, k, v = q
            # Square Root Decomposition
            if k >= B:
                for i in range(l, r + 1, k):
                    nums[i] = (nums[i] * v) % MOD
            else:   # (k < B) Atmost B unique k values
                smallKMap[k].append(q)

        for k in smallKMap:
            # Difference Array Theorem with Jumps
            diff = [1] * n
            for q in smallKMap[k]:
                l, r, _, v = q
                diff[l] = (diff[l] * v) % MOD
                steps = (r - l) // k
                out = l + ((steps + 1) * k)
                if out < n:
                    diff[out] = (diff[out] * self.power(v, MOD - 2)) % MOD  # Fermat's Little Theorem

            # Cumulative Product
            for i in range(n):
                if i - k >= 0:
                    diff[i] = (diff[i] * diff[i - k]) % MOD

            for i in range(n):
                nums[i] = (nums[i] * diff[i]) % MOD

        res = 0
        for num in nums:
            res = res ^ num
        return res