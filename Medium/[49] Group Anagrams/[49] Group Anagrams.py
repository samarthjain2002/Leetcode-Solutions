"""
Accepted
49 [Medium]
Runtime: 133 ms, faster than 9.71% of Python3 online submissions for Group Anagrams.
Memory Usage: 22.82 MB, less than 6.49% of Python3 online submissions for Group Anagrams.
"""
#   Without using defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Dict = {}
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            if tuple(count) not in Dict:
                Dict[tuple(count)] = [string]
            else:
                Dict[tuple(count)].append(string)

        return Dict.values()

"""
Accepted
49 [Medium]
Runtime: 148 ms, faster than 7.39% of Python3 online submissions for Group Anagrams.
Memory Usage: 23.08 MB, less than 5.98% of Python3 online submissions for Group Anagrams.
"""
#   By using defualtdict imported from collections
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Dict = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            Dict[tuple(count)].append(string)

        return Dict.values()