"""
Accepted
2375 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Construct Smallest Number From DI String.
Memory Usage: 18.08 MB, less than 6.63% of Python3 online submissions for Construct Smallest Number From DI String.
"""
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = [-1] * (len(pattern) + 1)
        used = set()

        def backtrack(i):
            if i == len(res):
                return True

            for j in range(1, 10):
                if j in used:
                    continue

                if i == 0:
                    res[0] = j
                    used.add(j)
                    if backtrack(i + 1):
                        return True
                    res[0] = -1
                    used.remove(j)
                elif pattern[i - 1] == 'I':
                    if j < res[i - 1]:
                        continue
                    else:
                        res[i] = j
                        used.add(j)
                        if backtrack(i + 1):
                            return True
                        res[i] = -1
                        used.remove(j)
                elif pattern[i - 1] == 'D':
                    if j > res[i - 1]:
                        continue
                    else:
                        res[i] = j
                        used.add(j)
                        if backtrack(i + 1):
                            return True
                        res[i] = -1
                        used.remove(j)
            return False

        backtrack(0)
        return "".join([str(i) for i in res])