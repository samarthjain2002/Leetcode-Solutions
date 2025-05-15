"""
Accepted
93 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Restore IP Addresses.
Memory Usage: 17.99 MB, less than 28.12% of Python3 online submissions for Restore IP Addresses.
"""
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        N = len(s)
        if N < 4 or N > 12:
            return []

        res = []
        def backtrack(string, index, byteCount):
            if byteCount > 4:
                return
            if index == len(s) and byteCount == 4:
                res.append(string[ : -1])
                return

            if index + 2 < N and s[index] != '0' and int(s[index : index + 3]) < 256:
                backtrack(string + s[index : index + 3] + '.', index + 3, byteCount + 1)
            if index + 1 < N and s[index] != '0':
                backtrack(string + s[index : index + 2] + '.', index + 2, byteCount + 1)
            if index < N:
                backtrack(string + s[index] + '.', index + 1, byteCount + 1)

        
        backtrack("", 0, 0)
        return res