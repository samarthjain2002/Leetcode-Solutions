"""
Accepted
1625 [Medium]
Runtime: 525 ms, faster than 82.73% of Python3 online submissions for Lexicographically Smallest String After Applying Operations.
Memory Usage: 19.43 MB, less than 62.59% of Python3 online submissions for Lexicographically Smallest String After Applying Operations.
"""
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        queue = deque([s])
        visited = set([s])
        smallest = s
        while queue:
            cur = queue.popleft()
            if cur < smallest:
                smallest = cur

            chars = list(cur)
            for i in range(1, len(chars), 2):
                chars[i] = str((int(chars[i]) + a) % 10)
            
            added = "".join(chars)
            if added not in visited:
                queue.append(added)
                visited.add(added)

            rotated = cur[-b : ] + cur[ : -b]
            if rotated not in visited:
                queue.append(rotated)
                visited.add(rotated)

        return smallest