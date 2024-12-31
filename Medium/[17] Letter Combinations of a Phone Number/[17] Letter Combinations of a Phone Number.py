"""
Accepted
17 [Medium]
Runtime: 737 ms, faster than 58.07% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 17.98 MB, less than 7.76% of Python3 online submissions for Letter Combinations of a Phone Number.
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        def backtrack(i, string):
            if i == len(digits):
                if string:
                    res.append(string)
                return

            for char in keyboard[digits[i]]:
                backtrack(i + 1, string + char)

        backtrack(0, "")
        return res