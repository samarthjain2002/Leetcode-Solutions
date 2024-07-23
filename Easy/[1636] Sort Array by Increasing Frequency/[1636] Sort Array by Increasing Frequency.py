"""
Accepted
1636 [Easy]
Runtime: 50 ms, faster than 55.36% of Python3 online submissions for Sort Array by Increasing Frequency.
Memory Usage:  16.64 MB, less than 12.04% of Python3 online submissions for Sort Array by Increasing Frequency.
"""
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freqMap = defaultdict(int)
        for num in nums:
            freqMap[num] += 1

        temp = [[val, key] for key, val in freqMap.items()]
        def custom_sort_condition(item):
            return item[0], -item[1]
        temp.sort(key = custom_sort_condition)
        
        res = []
        for i in temp:
            res += [i[1]] * i[0]
        return res