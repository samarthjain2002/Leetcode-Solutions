"""
Accepted
1122 [Easy]
Runtime: 35 ms, faster than 85.24% of Python3 online submissions for Relative Sort Array.
Memory Usage: 16.66 MB, less than 67.06% of Python3 online submissions for Relative Sort Array.
"""
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hashMap = defaultdict(int)
        for num in arr2:
            hashMap[num] = 0
        for num in arr1:
            if num in hashMap:
                hashMap[num] += 1
        arr2 = []
        for key, val in hashMap.items():
            for i in range(val):
                arr2.append(key)
        arr1.sort()
        for num in arr1:
            if num not in hashMap:
                arr2.append(num)
        return arr2