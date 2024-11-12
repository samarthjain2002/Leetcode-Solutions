"""
Accepted
2070 [Medium]
Runtime: 266 ms, faster than 42.68% of Python3 online submissions for Most Beautiful Item for Each Query.
Memory Usage: 66.03 MB, less than 61.83% of Python3 online submissions for Most Beautiful Item for Each Query.
"""
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        N = len(items)
        items.sort()

        maxBeauty = 0
        newItems = []
        for i in range(N):
            maxBeauty = max(maxBeauty, items[i][1])
            if newItems and newItems[-1][0] == items[i][0]:
                newItems[-1][1] = maxBeauty
            else:
                newItems.append([items[i][0], maxBeauty])
        N = len(newItems)

        def binarySearch(query):
            low, high = 0, N - 1
            while low <= high:
                mid = (low + high) // 2
                if newItems[mid][0] == query:
                    return mid
                elif newItems[mid][0] > query:
                    high = mid - 1
                else:
                    low = mid + 1
            return high

        res = []
        for query in queries:
            pos = binarySearch(query)
            if pos == -1:
                res.append(0)
            else:
                res.append(newItems[pos][1])
        return res