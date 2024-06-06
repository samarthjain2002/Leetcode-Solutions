"""
Accepted
846 [Medium]
Runtime: 160 ms, faster than 67.72% of Python3 online submissions for Hand of Straights.
Memory Usage:  18.45 MB, less than 50.76% of Python3 online submissions for Hand of Straights.
"""
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        dic = defaultdict(int)
        for card in hand:
            dic[card] += 1
        for card in hand:
            if dic[card]:
                for j in range(groupSize):
                    if not dic[card + j]:
                        return False
                    dic[card + j] -= 1
        return True