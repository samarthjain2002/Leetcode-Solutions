"""
Accepted
658 [Medium]
Runtime: 15 ms, faster than 39.64% of Python3 online submissions for Find K Closest Elements.
Memory Usage: 19.13 MB, less than 48.07% of Python3 online submissions for Find K Closest Elements.
"""
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x <= arr[0]:
            return arr[ : k]
        elif x >= arr[-1]:
            return arr[-k : ]

        res = deque()
        right = 0
        while x > arr[right]:
            right += 1
        left = right - 1

        for i in range(k):
            if left < 0:
                res.append(arr[right])
                right += 1
            elif right > len(arr) - 1:
                res.appendleft(arr[left])
                left -= 1
            else:
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    res.appendleft(arr[left])
                    left -= 1
                else:
                    res.append(arr[right])
                    right += 1
        
        return list(res)