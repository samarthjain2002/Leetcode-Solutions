"""
Accepted
1460 [Easy]
Runtime: 82 ms, faster than 16.17% of Python3 online submissions for Make Two Arrays Equal by Reversing Subarrays.
Memory Usage: 16.83 MB, less than 22.18% of Python3 online submissions for Make Two Arrays Equal by Reversing Subarrays.
"""
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        hashMap1 = defaultdict(int)
        hashMap2 = defaultdict(int)
        for i, num in enumerate(target):
            hashMap1[num] += 1
            hashMap2[arr[i]] += 1

        for key, val in hashMap1.items():
            if hashMap2[key] != val:
                return False
        return True