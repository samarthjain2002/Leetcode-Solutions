"""
Accepted
1298 [Hard]
Runtime: 15 ms, faster than 77.78% of Python3 online submissions for Maximum Candies You Can Get from Boxes.
Memory Usage: 28.19 MB, less than 65.13% of Python3 online submissions for Maximum Candies You Can Get from Boxes.
"""
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        queue = deque(initialBoxes)
        closed = set()      # Boxes available, but keys are not found
        res = 0
        while queue:
            boxID = queue.popleft()

            # If box can be opened
            if status[boxID]:
                res += candies[boxID]

                # Keys found
                for key in keys[boxID]:
                    status[key] = 1
                    if key in closed:
                        closed.remove(key)
                        queue.append(key)

                # New boxes found
                for newBox in containedBoxes[boxID]:
                    queue.append(newBox)
            else:
                closed.add(boxID)

        return res