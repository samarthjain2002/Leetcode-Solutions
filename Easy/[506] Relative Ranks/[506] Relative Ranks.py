"""
Accepted
506 [Easy]
Runtime: 58 ms, faster than 87.28% of Python3 online submissions for Relative Ranks.
Memory Usage: 17.88 MB, less than 39.79% of Python3 online submissions for Relative Ranks.
"""
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp = score.copy()
        dic = defaultdict(int)
        score.sort()
        score.reverse()
        for i, sc in enumerate(score):
            dic[sc] = i
        
        for i in range(len(temp)):
            if dic[temp[i]] == 0:
                temp[i] = "Gold Medal"
            elif dic[temp[i]] == 1:
                temp[i] = "Silver Medal"
            elif dic[temp[i]] == 2:
                temp[i] = "Bronze Medal"
            else:
                temp[i] = str(dic[temp[i]] + 1)

        return temp