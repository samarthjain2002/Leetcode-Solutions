"""
Accepted
3318 [Easy]
Runtime: 21 ms, faster than 81.56% of Python3 online submissions for Find X-Sum of All K-Long Subarrays I.
Memory Usage: 18.00 MB, less than 38.70% of Python3 online submissions for Find X-Sum of All K-Long Subarrays I.
"""
# TC: O((n+k+1)klogk), SC: O(n+k)
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        for i in range(len(nums) - k + 1):
            hashMap = Counter(nums[i : i + k])
            if len(hashMap) <= x:
                res.append(sum(nums[i : i + k]))
            else:
                pairs = list(hashMap.items())
                pairs.sort(key=lambda p: (p[1], p[0]), reverse=True)
                curSum = 0
                for num, count in pairs[ : x]:
                    curSum += num * count
                res.append(curSum)
        return res