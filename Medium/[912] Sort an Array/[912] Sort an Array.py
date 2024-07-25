"""
Accepted
912 [Medium]
Runtime: 1262 ms, faster than 60.12% of Python3 online submissions for Sort an Array.
Memory Usage: 24.12 MB, less than 62.39% of Python3 online submissions for Sort an Array.
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(data, start, end):
            if start < end:
                mid = (start + end) // 2
                mergeSort(data, start, mid)
                mergeSort(data, mid + 1, end)
                merge(data, start, mid, end)
            return data
                
        def merge(data, start, mid, end):
            i, j, k = start, mid + 1, 0
            temp = [0] * (end - start + 1)
            while i <= mid and j <= end:
                if data[i] < data[j]:
                    temp[k] = data[i]
                    i += 1
                    k += 1
                else:
                    temp[k] = data[j]
                    j += 1
                    k += 1
            while i <= mid:
                temp[k] = data[i]
                i += 1
                k += 1
            while j <= end:
                temp[k] = data[j]
                j += 1
                k += 1
            for i in range(start, end + 1):
                data[i] = temp[i - start]

        return mergeSort(nums, 0, len(nums) - 1)