"""
Accepted
1718 [Medium]
Runtime: 5 ms, faster than 56.25% of Python3 online submissions for Construct the Lexicographically Largest Valid Sequence.
Memory Usage: 17.62 MB, less than 89.84% of Python3 online submissions for Construct the Lexicographically Largest Valid Sequence.
"""
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [-1] * ((n * 2) - 1)
        used = set()

        def backtrack(index):
            while index < len(res) and res[index] != -1:
                index += 1

            if index == len(res):
                return True

            for maxEle in range(n, 0, -1):
                if maxEle in used:
                    continue

                if maxEle == 1:
                    res[index] = 1
                    used.add(1)
                    if backtrack(index + 1):
                        return True
                    res[index] = -1
                    used.remove(1)
                elif (index + maxEle) < len(res) and res[index + maxEle] == -1:
                    res[index] = res[index + maxEle] = maxEle
                    used.add(maxEle)
                    if backtrack(index + 1):
                        return True
                    res[index] = res[index + maxEle] = -1
                    used.remove(maxEle)
            return False

        backtrack(0)
        return res