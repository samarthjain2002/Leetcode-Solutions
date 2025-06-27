"""
Accepted
724 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Find Pivot Index.
Memory Usage: 18.04 MB, less than 9.96% of Python3 online submissions for Find Pivot Index.
"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        prefixSums = [nums[0]]
        for i in range(1, len(nums)):
            prefixSums.append(prefixSums[-1] + nums[i])
        print(prefixSums)
            
        for i in range(len(prefixSums)):
            if i == 0 and prefixSums[-1] - prefixSums[i] == 0:
                print(prefixSums[-1], prefixSums[i], prefixSums[-1] - prefixSums[i])
                return i
            elif i == len(prefixSums) - 1 and prefixSums[i - 1] == 0:
                return i
            elif i not in [0, len(prefixSums) - 1] and prefixSums[-1] - prefixSums[i] == prefixSums[i - 1]:
                return i
        return -1



"""
Runtime: 11 ms, faster than 32.30% of Python3 online submissions for Find Pivot Index.
Memory Usage: 19.58 MB, less than 7.16% of Python3 online submissions for Find Pivot Index.
"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftTotal = rightTotal = 0
        leftPrefixSums = []
        rightPrefixSums = [0] * len(nums)
        for i in range(len(nums)):
            leftPrefixSums.append(leftTotal)
            rightPrefixSums[len(nums) - i - 1] = rightTotal

            leftTotal += nums[i]
            rightTotal += nums[len(nums) - i - 1]
        
        for i in range(len(nums)):
            if leftPrefixSums[i] == rightPrefixSums[i]:
                return i
        return -1