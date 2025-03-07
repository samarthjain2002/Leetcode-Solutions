"""
Accepted
2523 [Medium]
Runtime: 1576 ms, faster than 46.25% of Python3 online submissions for Closest Prime Numbers in Range.
Memory Usage: 35.16 MB, less than 18.13% of Python3 online submissions for Closest Prime Numbers in Range.
"""
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Sieve of Eratosthenes
        def get_primes():
            is_prime = [True] * (right + 1)
            is_prime[0] = is_prime[1] = False

            for n in range(2, int(sqrt(right)) + 1):
                if not is_prime[n]:
                    continue
                for m in range(n * 2, len(is_prime), n):
                    is_prime[m] = False

            primes = []
            for i in range(left, len(is_prime)):
                if is_prime[i]:
                    primes.append(i)
            return primes
            

        primes = get_primes()
        res = [-1, -1]
        diff = float("inf")
        for i in range(1, len(primes)):
            if primes[i] - primes[i - 1] < diff:
                diff = primes[i] - primes[i - 1]
                res[0], res[1] = primes[i - 1], primes[i]
        return res