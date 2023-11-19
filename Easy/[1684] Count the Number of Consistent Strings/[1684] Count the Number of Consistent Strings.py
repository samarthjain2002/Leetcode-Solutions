"""
Accepted
1684 [Easy]
Runtime: 257 ms, faster than 30.49% of Python3 online submissions for Count the Number of Consistent Strings.
Memory Usage: 18.29 MB, less than 85.31% of Python3 online submissions for Count the Number of Consistent Strings.
"""
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        list1 = []
        count = len(words)
        for i in allowed:
            list1.append(i)

        for i in range(0,len(words)):
            for j in range(0,len(words[i])):
                if words[i][j] not in list1:
                    i += 1
                    count -= 1
                    break
            
        return count