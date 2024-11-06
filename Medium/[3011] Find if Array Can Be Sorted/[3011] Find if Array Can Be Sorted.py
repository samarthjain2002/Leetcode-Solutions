"""
Accepted
3011 [Medium]
Runtime: 13 ms, faster than 45.45% of Python3 online submissions for Find if Array Can Be Sorted.
Memory Usage:  16.78 MB, less than 23.35% of Python3 online submissions for Find if Array Can Be Sorted.
"""
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        N = len(nums)

        numBits, prefixSums = [], []
        for i, num in enumerate(nums):
            numBits.append([bin(num).count('1'), num])
            if i == 0:
                prefixSums.append(numBits[i][0])
            else:
                prefixSums.append(numBits[i][0] + prefixSums[i - 1])

        nums.sort()
        sortedPos = defaultdict(int)
        for i, num in enumerate(nums):
            sortedPos[num] = i

        for i in range(N):
            left, right = min(i, sortedPos[numBits[i][1]]), max(i, sortedPos[numBits[i][1]])
            if left == 0 and prefixSums[right] != numBits[i][0] * (right + 1):
                return False
            elif left != 0 and prefixSums[right] - prefixSums[left - 1] != numBits[i][0] * (right - left + 1):
                return False
        return True