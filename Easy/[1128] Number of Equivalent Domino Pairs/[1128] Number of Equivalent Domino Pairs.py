"""
Accepted
1128 [Easy]
Runtime: 7 ms, faster than 92.01% of Python3 online submissions for Number of Equivalent Domino Pairs.
Memory Usage: 24.33 MB, less than 43.37% of Python3 online submissions for Number of Equivalent Domino Pairs.
"""
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