"""
Accepted
556 [Medium]
Runtime: 36 ms, faster than 49.20% of Python3 online submissions for Next Greater Element III.
Memory Usage: 16.52 MB, less than 41.38% of Python3 online submissions for Next Greater Element III.
"""
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n < 10:
            return -1

        nums = [int(dig) for dig in str(n)]
        
        N = len(nums)

        pivot = N
        if N > 1:
            for i in range(N - 2, -1, -1):
                if nums[i] < nums[i + 1]:
                    pivot = i
                    break

        if pivot != N:
            if nums[pivot] >= nums[-1]:
                for i in range(N - 1, -1, -1):
                    if nums[i] > nums[pivot]:
                        temp = nums[pivot]
                        nums[pivot] = nums[i]
                        nums[i] = temp
                        break
                nums[:] = nums[ : pivot + 1] + list(reversed(nums[pivot + 1 : ]))
            else:
                nums[:] = nums[ : pivot + 1] + list(reversed(nums[pivot + 1 : ]))
                temp = nums[pivot]
                nums[pivot] = nums[pivot + 1]
                nums[pivot + 1] = temp
        else:
            return -1

        res = ""
        for dig in nums:
            res += str(dig)

        if int(res) > 2147483647:
            return -1
        else:
            return int(res)