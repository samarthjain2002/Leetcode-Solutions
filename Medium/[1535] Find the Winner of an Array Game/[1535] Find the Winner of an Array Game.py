"""
Accepted
1535 [Medium]
Runtime: 533 ms, faster than 58.70% of Python3 online submissions for Find the Winner of an Array Game.
Memory Usage: 29.89 MB, less than 67.39% of Python3 online submissions for Find the Winner of an Array Game.
"""
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        left = 0
        right = 1
        
        winner = arr[0]
        win_count = 0
        maximum = max(arr)

        while win_count != k:
            if arr[left] == maximum:
                return winner
            if arr[left] > arr[right]:
                win_count += 1
                right += 1
            else:
                win_count = 1
                winner = arr[right]
                left = right
                right += 1

        return winner