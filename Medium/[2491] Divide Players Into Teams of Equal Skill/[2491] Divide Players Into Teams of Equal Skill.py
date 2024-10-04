"""
Accepted
2491 [Medium]
Runtime: 395 ms, faster than 73.80% of Python3 online submissions for Divide Players Into Teams of Equal Skill.
Memory Usage: 29.39 MB, less than 94.16% of Python3 online submissions for Divide Players Into Teams of Equal Skill.
"""
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        sk = skill[0] + skill[-1]
        res = 0
        for i in range(len(skill) // 2):
            thisTeam = skill[i] + skill[-1 - i]
            if thisTeam != sk:
                return -1
            res += skill[i] * skill[-1 - i]
        return res