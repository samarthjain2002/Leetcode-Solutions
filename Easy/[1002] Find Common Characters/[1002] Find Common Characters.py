"""
Accepted
1002 [Easy]
Runtime: 57 ms, faster than 21.70% of Python3 online submissions for Find Common Characters.
Memory Usage: 16.58 MB, less than 93.72% of Python3 online submissions for Find Common Characters.
"""
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        firstHMap = defaultdict(int)
        for char in words[0]:
            firstHMap[char] += 1
        
        for word in words[1:]:
            newHMap = defaultdict(int)
            for char in word:
                newHMap[char] += 1
            
            for key, val in firstHMap.items():
                if firstHMap[key] > newHMap[key]:
                    firstHMap[key] = newHMap[key]

        res = []
        for key, val in firstHMap.items():
            if val > 0:
                for i in range(val):
                    res.append(key)
        return res