"""
Accepted
1497 [Medium]
Runtime: 470 ms, faster than 88.48% of Python online submissions for Check If Array Pairs Are Divisible by k.
Memory Usage: 30.36 MB, less than 73.50% of Python online submissions for Check If Array Pairs Are Divisible by k.
"""
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        for i, num in enumerate(arr):
            arr[i] = num % k

        count = [0] * k
        for num in arr:
            count[num] += 1
            
        for i, num in enumerate(count):
            if i == 0:
                if num % 2 != 0:
                    return False
            elif num != count[k - i]:
                return False
        return True