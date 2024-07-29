"""
Accepted
1395 [Medium]
Runtime: 827 ms, faster than 11.12% of Python3 online submissions for Count Number of Teams.
Memory Usage: 16.59 MB, less than 92.36% of Python3 online submissions for Count Number of Teams.
"""
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        N = len(rating)
        left_smaller = [0] * N
        left_larger = [0] * N
        right_smaller = [0] * N
        right_larger = [0] * N

        for i in range(N):
            for j in range(i):
                if rating[j] < rating[i]:
                    left_smaller[i] += 1
                if rating[j] > rating[i]:
                    left_larger[i] += 1
        
        for i in range(N):
            for j in range(i + 1, N):
                if rating[i] < rating[j]:
                    right_larger[i] += 1
                if rating[i] > rating[j]:
                    right_smaller[i] += 1

        count = 0
        for i in range(N):
            count += left_smaller[i] * right_larger[i] + left_larger[i] * right_smaller[i]
        return count