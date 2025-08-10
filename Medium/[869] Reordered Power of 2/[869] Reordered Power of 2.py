"""
Accepted
869 [Medium]
Runtime: 4 ms, faster than 42.37% of Python3 online submissions for Reordered Power of 2.
Memory Usage: 17.90 MB, less than 35.50% of Python3 online submissions for Reordered Power of 2.
"""
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        nDigits = defaultdict(int)
        for dig in str(n):
            nDigits[dig] += 1

        def helper():
            for dig, freq in nDigits.items():
                if sqDigits[dig] != freq:
                    return False

            for dig, freq in sqDigits.items():
                if nDigits[dig] != freq:
                    return False

            return True

        sqDigits = defaultdict(int)
        for exp in range(31):
            sq = 2**exp
            for dig in str(sq):
                sqDigits[dig] += 1

            if helper():
                return True

            sqDigits.clear()

        return False