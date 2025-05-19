"""
Accepted
767 [Medium]
Runtime: 43 ms, faster than 19.35% of Python3 online submissions for Reorganize String.
Memory Usage: 16.44 MB, less than 93.30% of Python3 online submissions for Reorganize String.
"""
class Solution:
    def reorganizeString(self, s: str) -> str:
        # Build charMap
        charFreq = defaultdict(int)
        for char in s:
            charFreq[char] += 1

        # Add all frequency to max heap
        maxHeap = []
        for char, freq in charFreq.items():
            heapq.heappush(maxHeap, (-freq, char))

        # Build res
        res = ""
        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            if res and res[-1] == char:
                # If there is no other character
                if not maxHeap:
                    return ""

                count2, char2 = heapq.heappop(maxHeap)
                res += char2
                count2 += 1     # Since count is -ve of actual count
                # If count2 is not 0
                if count2:
                    heapq.heappush(maxHeap, (count2, char2))
            else:
                res += char
                count += 1

            # If count is not 0
            if count:
                heapq.heappush(maxHeap, (count, char))
                
        return res