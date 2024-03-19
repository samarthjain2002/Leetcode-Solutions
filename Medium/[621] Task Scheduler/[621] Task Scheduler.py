"""
Accepted
621 [Medium]
Runtime: 357 ms, faster than 84.27% of Python3 online submissions for Task Scheduler.
Memory Usage:  17.18 MB, less than 59.31% of Python3 online submissions for Task Scheduler.
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = list(Counter(tasks).values())
        maxElement = max(freq)
        numOfMaxElement = freq.count(maxElement)

        # Calculate the number of intervals required for tasks without the max frequency
        num_intervals = (maxElement - 1) * (n + 1)

        # Add the tasks with the same maximum frequency
        num_intervals += numOfMaxElement

        # Handle the case where there might be idle intervals at the end
        return max(num_intervals, len(tasks))