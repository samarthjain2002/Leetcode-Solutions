"""
Accepted
1824 [Medium]
Runtime: 1719 ms, faster than 42.13% of Python3 online submissions for Minimum Sideway Jumps.
Memory Usage: 39.59 MB, less than 99.61% of Python3 online submissions for Minimum Sideway Jumps.
"""
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        lanes = [1, 0, 1]

        for i in range(1, len(obstacles)):
            new_lanes = [float("inf")] * 3
            for j in range(3):
                if obstacles[i] - 1 != j and lanes[j] != float("inf"):
                    # Move ahead with no extra cost
                    new_lanes[j] = lanes[j]

            for j in range(3):
                if obstacles[i] - 1 != j and new_lanes[j] == float("inf"):
                    # Jump to this cell with 1 extra cost
                    new_lanes[j] = min(new_lanes) + 1

            lanes = new_lanes

        return min(lanes)