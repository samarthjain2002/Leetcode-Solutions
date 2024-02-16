"""
Accepted
1481 [Medium]
Runtime: 473 ms, faster than 25.08% of Python3 online submissions for Least Number of Unique Integers after K Removals.
Memory Usage: 34.92 MB, less than 45.49% of Python3 online submissions for Least Number of Unique Integers after K Removals.
"""
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freqMap = [[count, num] for num, count in Counter(arr).items()]
        freqMap.sort()
        N = len(freqMap)
        for i in range(N):
            if k == 0:
                break
            if freqMap[i][0] >= k:
                freqMap[i][0] -= k
                k = 0
            else:
                k -= freqMap[i][0]
                freqMap[i][0] = 0

        count = 0
        for i in range(N):
            if freqMap[i][0] != 0:
                count += 1
        
        return count