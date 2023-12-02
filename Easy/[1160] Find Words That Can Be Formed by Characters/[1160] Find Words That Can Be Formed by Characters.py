"""
Accepted
1160 [Easy]
Runtime: 370 ms, faster than 5.01% of Python3 online submissions for Find Words That Can Be Formed by Characters.
Memory Usage: 16.98 MB, less than 13.86% of Python3 online submissions for Find Words That Can Be Formed by Characters.
"""
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        characs = {}
        for i in chars:
            if i not in characs:
                characs[i] = 1
            else:
                characs[i] += 1

        res = 0
        for i in range(0,len(words)):
            match = copy.deepcopy(characs)
            for j in range(0,len(words[i])):
                if words[i][j] not in match or match[words[i][j]] == 0:
                    break
                else:
                    if j == len(words[i]) - 1:
                        res += len(words[i])
                        break
                    match[words[i][j]] -= 1

        return res