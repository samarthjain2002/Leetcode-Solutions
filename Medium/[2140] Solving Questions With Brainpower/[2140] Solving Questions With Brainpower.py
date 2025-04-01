"""
Accepted
2140 [Medium]
Runtime: 87 ms, faster than 64.73% of Python3 online submissions for Solving Questions With Brainpower.
Memory Usage: 60.94 MB, less than 50.81% of Python3 online submissions for Solving Questions With Brainpower.
"""
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * len(questions)
        dp[-1] = questions[-1][0]

        for i in reversed(range(len(questions) - 1)):
            answer = questions[i][0]
            if i + questions[i][1] + 1 < len(questions):
                answer += dp[i + questions[i][1] + 1]
            dp[i] = max(answer, dp[i + 1])
            
        return dp[0]