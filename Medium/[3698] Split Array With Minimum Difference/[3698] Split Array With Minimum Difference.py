"""
Accepted
3698 [Medium]
Runtime: 104 ms, faster than 66.18% of Python3 online submissions for Split Array With Minimum Difference.
Memory Usage: 31.07 MB less than 57.19% of Python3 online submissions for Split Array With Minimum Difference.
"""
class Solution:
    def splitArray(self, nums: List[int]) -> int:
        leftValid, rightValid = 0, len(nums) - 1
        curMin = -1
        for i in range(len(nums)):
            if nums[i] <= curMin:
                break
            curMin = nums[i]
            leftValid = i

        curMin = -1
        for i in reversed(range(len(nums))):
            if nums[i] <= curMin:
                break
            curMin = nums[i]
            rightValid = i

        prefixSums = [nums[0]]
        for i in range(1, len(nums)):
            prefixSums.append(prefixSums[i - 1] + nums[i])

        res = float("inf")
        for i in range(max(0, rightValid - 1), leftValid + 1):
            res = min(res, abs(prefixSums[i] - (prefixSums[-1] - prefixSums[i])))

        return res if res < float("inf") else -1



"""
Runtime: 340 ms, faster than 5.14% of Python3 online submissions for Split Array With Minimum Difference.
Memory Usage: 33.07 MB less than 17.44% of Python3 online submissions for Split Array With Minimum Difference.
"""
class Solution:
    def splitArray(self, nums: List[int]) -> int:
        N = len(nums)

        inc, dec = [False] * len(nums), [False] * len(nums)
        curMin1 = curMin2 = -1
        for i in range(len(nums)):
            if curMin1 < nums[i]:
                inc[i] = True
                curMin1 = nums[i]
            else:
                curMin1 = float("inf")

            if curMin2 < nums[N - i - 1]:
                dec[N - i - 1] = True
                curMin2 = nums[N - i - 1]
            else:
                curMin2 = float("inf")

        prefixSums = [nums[0]]
        for i in range(1, len(nums)):
            prefixSums.append(prefixSums[i - 1] + nums[i])

        res = float("inf")
        for i in range(len(nums) - 1):
            if inc[i] and dec[i + 1]:
                res = min(res, abs(prefixSums[i] - (prefixSums[-1] - prefixSums[i])))

        return res if res < float("inf") else -1