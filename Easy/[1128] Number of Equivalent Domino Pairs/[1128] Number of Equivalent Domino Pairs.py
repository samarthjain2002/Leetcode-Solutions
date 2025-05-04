"""
Accepted
1128 [Easy]
Runtime: 2 ms, faster than 99.71% of Python3 online submissions for Number of Equivalent Domino Pairs.
Memory Usage: 24.07 MB, less than 98.57% of Python3 online submissions for Number of Equivalent Domino Pairs.
"""
# TC: O(n), SC: O(1)
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        domId = [0] * 100
        res = 0
        for a, b in dominoes:
            # Turn any domino (a, b) or (b, a) into same ID
            ID = a * 10 + b if a >= b else b * 10 + a
            # Add the previous count to result
            res += domId[ID]
            # Increment the count of ID pairs
            domId[ID] += 1
        return res



"""
Runtime: 7 ms, faster than 92.01% of Python3 online submissions for Number of Equivalent Domino Pairs.
Memory Usage: 24.33 MB, less than 43.37% of Python3 online submissions for Number of Equivalent Domino Pairs.
"""
# TC: O(n), SC: O(n)
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        hashMap = defaultdict(int)
        for dom in dominoes:
            if tuple(dom) in hashMap:
                hashMap[tuple(dom)] += 1
            elif tuple([dom[1], dom[0]]) in hashMap:
                hashMap[tuple([dom[1], dom[0]])] += 1
            else:
                hashMap[tuple(dom)] += 1
            
        res = 0
        for dom, freq in hashMap.items():
            res += (freq * (freq - 1)) // 2
        return res