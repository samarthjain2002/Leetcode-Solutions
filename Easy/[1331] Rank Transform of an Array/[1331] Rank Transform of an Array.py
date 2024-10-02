"""
Accepted
1331 [Easy]
Runtime: 243 ms, faster than 56.11% of Python3 online submissions for Rank Transform of an Array.
Memory Usage: 33.15 MB, less than 89.62% of Python3 online submissions for Rank Transform of an Array.
"""
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr) == 0:
            return arr

        newArr = arr.copy()
        newArr.sort()

        ranks = {}
        rank = 1
        ranks[newArr[0]] = 1
        for i in range(1, len(newArr)):
            if newArr[i] > newArr[i - 1]:
                rank += 1
                ranks[newArr[i]] = rank
                
        for i, num in enumerate(arr):
            arr[i] = ranks[num]
        return arr