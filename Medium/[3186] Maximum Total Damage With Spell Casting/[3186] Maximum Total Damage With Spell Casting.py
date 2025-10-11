"""
Accepted
3186 [Medium]
Runtime: 466 ms, faster than 70.00% of Python3 online submissions for Maximum Total Damage With Spell Casting.
Memory Usage: 41.56 MB, less than 63.75% of Python3 online submissions for Maximum Total Damage With Spell Casting.
"""
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freqMap = Counter(power)
        power = sorted(list(set(power)))
        dp = [freqMap[spell] * spell for spell in power]
        for i, spell in enumerate(power):
            if i > 0 and power[i - 1] < spell - 2:
                dp[i] += dp[i - 1]
            elif i > 1 and power[i - 2] < spell - 2:
                dp[i] += dp[i - 2]
            elif i > 2 and power[i - 3] < spell - 2:
                dp[i] += dp[i - 3]
            
            if i > 0:
                dp[i] = max(dp[i], dp[i - 1])
                
        return max(dp)