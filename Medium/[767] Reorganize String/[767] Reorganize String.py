"""
Accepted
767 [Medium]
Runtime: 43 ms, faster than 19.35% of Python3 online submissions for Reorganize String.
Memory Usage: 16.44 MB, less than 93.30% of Python3 online submissions for Reorganize String.
"""
class Solution:
    def reorganizeString(self, s: str) -> str:
        hashMap = defaultdict(int)
        for char in s:
            hashMap[char] += 1
        
        maxHeap = []
        for key, val in hashMap.items():
            heapq.heappush(maxHeap, (-val, key))

        res = ""
        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            if len(res) >= 1 and res[-1] == char:
                if not maxHeap:
                    return ""
                count2, char2 = heapq.heappop(maxHeap)
                res += char2
                count2 += 1
                if count2:
                    heapq.heappush(maxHeap, (count2, char2))
            else:
                res += char
                count += 1
            if count:
                heapq.heappush(maxHeap, (count, char))
        return res