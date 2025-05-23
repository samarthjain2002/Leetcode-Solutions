"""
Accepted
3068 [Hard]
Runtime: 43 ms, faster than 63.79% of Python3 online submissions for Find the Maximum Sum of Node Values.
Memory Usage: 26.20 MB, less than 58.62% of Python3 online submissions for Find the Maximum Sum of Node Values.
"""
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        """
        Observations
        1) num ^ k ^ k = num. So, if we want to increase num, we have to XOR it with k atmost once.
        2) If we XOR all the nums in a path, only the nums in the ends of the path change, since obs1.
        3) Since the graph is a tree and connected, we can XOR any and exactly 2 nodes at a time.
        4) Try to find pair of nodes which will increase on XOR
        5) No need for a heap, since we only XOR a node once.
        6 ) Simply sort the nodes after the XOR and add it to result.
        """
        delta = [(num ^ k) - num for num in nums]
        delta.sort(reverse = True)
        res = sum(nums)

        for i in range(0, len(delta), 2):
            if i == len(delta) - 1:
                break

            path_delta = delta[i] + delta[i + 1]
            if path_delta < 0:
                break

            res += path_delta

        return res