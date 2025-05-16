"""
Accepted
31 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Next Permutation.
Memory Usage: 17.75 MB, less than 56.66% of Python3 online submissions for Next Permutation.
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Finding the pivot
        pivot = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                pivot = i - 1
                break

        # If there is not pivot, it is already the maximal lexicographic permutation
        # Reverse the whole array
        if pivot == -1:
            left, right = 0, len(nums) - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        # Pivot is found
        else:
            # Find the next bigger element than the pivot and exchange their places
            right = len(nums) - 1
            while nums[right] <= nums[pivot]:
                right -= 1
            nums[pivot], nums[right] = nums[right], nums[pivot]

            # Now reverse the array
            left, right = pivot + 1, len(nums) - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1



"""
Runtime: 44 ms, faster than 0.33% of Python3 online submissions for Next Permutation.
Memory Usage: 16.61 MB, less than 100.00% of Python3 online submissions for Next Permutation.
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
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
            nums[:] = reversed(nums)