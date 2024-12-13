"""
Accepted
4 [Hard]
Runtime: 3 ms, faster than 53.33% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage:  17.74 MB, less than 7.29% of Python3 online submissions for Median of Two Sorted Arrays.
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        M, N = len(nums1), len(nums2)
        # len(A) <= len(B)
        if M <= N:
            A, B = nums1, nums2
        else:
            A, B = nums2, nums1
            M, N = N, M
        total = M + N       # Length of merged, sorted array
        half = total // 2

        left, right = 0, M - 1      # Binary search on array A
        while True:
            Amid = left + ((right - left) // 2)
            Bmid = half - Amid - 2      # -2 for 0-indexing of array A and B

            Aleft = A[Amid] if Amid >= 0 else float("-inf")
            Aright = A[Amid + 1] if (Amid + 1) < M else float("inf")
            Bleft = B[Bmid] if Bmid >= 0 else float("-inf")
            Bright = B[Bmid + 1] if (Bmid + 1) < N else float("inf")

            # If partitioned correctly
            if Aleft <= Bright and Bleft <= Aright:
                # If length of merged, sorted array is odd
                if total % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # If partition requires more elements from A
            elif Bleft > Aright:
                left = Amid + 1
            # If partition requires less elements from A
            else:
                right = Amid - 1