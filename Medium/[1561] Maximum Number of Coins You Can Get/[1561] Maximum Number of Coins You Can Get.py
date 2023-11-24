"""
Accepted
1561 [Medium]
Runtime: 534 ms, faster than 38.59% of Java online submissions for Maximum Number of Coins You Can Get.
Memory Usage: 28.72 MB, less than 21.94% of Java online submissions for Maximum Number of Coins You Can Get.
"""
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()

        count = 0
        for i in range(len(piles)-1,int(len(piles)/3)-1,-1):
            if len(piles) % 2 == 0 and i % 2 == 0:
                count += piles[i]
            elif len(piles) % 2 != 0 and i % 2 != 0:
                count += piles[i]

        return count