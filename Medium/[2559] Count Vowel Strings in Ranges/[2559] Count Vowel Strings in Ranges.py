"""
Accepted
2559 [Medium]
Runtime: 510 ms, faster than 65.01% of Python3 online submissions for Count Vowel Strings in Ranges.
Memory Usage: 57.37 MB, less than 58.97% of Python3 online submissions for Count Vowel Strings in Ranges.
"""
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        prefixSums = [0] * len(words)
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                if i == 0:
                    prefixSums[i] = 1
                prefixSums[i] = prefixSums[i - 1] + 1
            else:
                if i == 0:
                    continue
                prefixSums[i] = prefixSums[i - 1]

        res = [0] * len(queries)
        for i, query in enumerate(queries):
            if query[0] == 0:
                res[i] = prefixSums[query[1]]
            else:
                res[i] = prefixSums[query[1]] - prefixSums[query[0] - 1]
        return res