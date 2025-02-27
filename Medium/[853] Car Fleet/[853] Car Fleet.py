"""
Accepted
853 [Medium]
Runtime: 601 ms, faster than 31.25% of Python3 online submissions for Car Fleet.
Memory Usage: 30.29 MB, less than 28.92% of Python3 online submissions for Car Fleet.
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[pos, sp] for pos, sp in zip(position, speed)]

        stack = []
        for pos, sp in sorted(pair)[::-1]:
            stack.append((target - pos) / sp)
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)