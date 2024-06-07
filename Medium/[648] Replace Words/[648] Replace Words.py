"""
Accepted
648 [Medium]
Runtime: 449 ms, faster than 9.49% of Python3 online submissions for Replace Words.
Memory Usage:  24.93 MB, less than 81.26% of Python3 online submissions for Replace Words.
"""
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        hashSet = set(dictionary)
        res, string = "", ""
        flag = False
        for i, char in enumerate(sentence):
            if flag:
                if char != ' ':
                    continue
                else:
                    flag = False
                    continue
            if char == ' ':
                res += string + ' '
                string = ""
            else:
                string += char
                if string in hashSet:
                    res += string + ' '
                    string = ""
                    flag = True
                elif i == len(sentence) - 1:
                    res += string
        return res if res[-1] != ' ' else res[:-1]