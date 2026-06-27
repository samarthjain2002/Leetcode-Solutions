"""
Accepted
3020 [Medium]
Runtime: 349 ms, faster than 12.60% of Python3 online submissions for Find the Maximum Number of Elements in Subset.
Memory Usage: 31.76 MB, less than 49.61% of Python3 online submissions for Find the Maximum Number of Elements in Subset.
"""
# Hash Table + Enumeration + BruteForce Solution
# TC: O(nlog(log(M)), SC: O(n)
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # Count the frequency of every number
        freq = Counter(nums)

        max_length = 0
        # Try starting the sequence from every number
        for start in nums:

            # Check the chain
            # start -> start² -> start⁴ -> start⁸ -> ...
            #  Maximum exponent needed is small (<= 5) because of constraints
            for level in range(6):
                current = start**(2**level)

                # Chain breaks because the number doesn't exist
                if current not in freq:
                    # We can only use complete pairs before this point
                    max_length = max(max_length, level*2 - 1)
                    break

                # Number exists only once
                elif freq[current] == 1:
                    # This number can be placed in the center
                    max_length = max(max_length, level*2 + 1)
                    break

        # Handle the special case for 1 separately
        # Since 1² = 1 forever, we can use all 1s if the count is odd,
        # otherwise one must be discarded
        if freq[1] % 2:
            max_length = max(max_length, freq[1])
        else:
            max_length = max(max_length, freq[1] - 1)
                    
        return max_length