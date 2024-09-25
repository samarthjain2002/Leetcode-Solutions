"""
Accepted
2416 [Hard]
Runtime: 3762 ms, faster than 9.32% of Python3 online submissions for Sum of Prefix Scores of Strings.
Memory Usage: 598.42 MB, less than 8.97% of Python3 online submissions for Sum of Prefix Scores of Strings.
"""
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        hashMap = defaultdict(int)

        for word in words:
            for i in range(1, len(word) + 1):
                hashMap[word[ : i]] += 1
        
        res = [0] * len(words) 
        for i, word in enumerate(words):
            for j in range(1, len(word) + 1):
                res[i] += hashMap[word[ : j]]
        return res