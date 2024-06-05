"""
Accepted
68 [Hard]
Runtime: 30 ms, faster than 90.24% of Python3 online submissions for Text Justification.
Memory Usage: 16.66 MB, less than 55.10% of Python3 online submissions for Text Justification.
"""
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        w = [[]]
        length = 0
        for word in words:
            if length + len(word) <= maxWidth:
                w[-1].append(word)
                length += len(word) + 1
            else:
                w.append([word])
                length = len(word) + 1

        res = []
        for i, wline in enumerate(w):
            wordCount = len(wline)
            if wordCount == 1:
                res.append(wline[0])
                res[-1] += (maxWidth - len(wline[0])) * ' '
            elif i == len(w) - 1:
                res.append("")
                for i, wor in enumerate(wline):
                    res[-1] += wor
                    if i != wordCount - 1:
                        res[-1] += ' '
                res[-1] += (maxWidth - len(res[-1])) * ' '
            else:
                res.append("")
                wordLen = 0
                for wor in wline:
                    wordLen += len(wor)
                spaces = maxWidth - wordLen
                for wor in wline:
                    res[-1] += wor
                    if wordCount > 1:
                        if spaces % (wordCount - 1) != 0:
                            res[-1] += ((spaces // (wordCount - 1)) + 1) * ' '
                            spaces -= ((spaces // (wordCount - 1)) + 1)
                        else:
                            res[-1] += (spaces // (wordCount - 1)) * ' '
                            spaces -= (spaces // (wordCount - 1))
                        wordCount -= 1
        return res