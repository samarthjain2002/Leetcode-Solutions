"""
Accepted
726 [Hard]
Runtime: 37 ms, faster than 48.22% of Python3 online submissions for Number of Atoms.
Memory Usage: 16.62 MB, less than 28.74% of Python3 online submissions for Number of Atoms.
"""
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        N = len(formula)
        stack = [defaultdict(int)]
        i = 0
        while i < N:
            if formula[i] == '(':
                stack.append(defaultdict(int))
            elif formula[i] == ')':
                count = ""
                while i + 1 < N and formula[i + 1].isdigit():
                    count += formula[i + 1]
                    i += 1
                count = 1 if not count else int(count)
                for element in stack[-1]:
                    stack[-2][element] += stack[-1][element] * count
                stack.pop()
            else:
                element = formula[i]
                count = ""
                if i + 1 < N and formula[i + 1].islower():
                    element += formula[i + 1]
                    i += 1
                while i + 1 < N and formula[i + 1].isdigit():
                    count += formula[i + 1]
                    i += 1
                count = 1 if not count else int(count)
                stack[-1][element] += count
            i += 1

        res = ""
        stack[-1] = dict(sorted(stack[-1].items()))
        for key, val in stack[-1].items():
            res += key + str(val) if val != 1 else key
        return res