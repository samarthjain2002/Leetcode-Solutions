"""
Accepted
1514 [Medium]
Runtime: 127 ms, faster than 32.78% of Python online submissions for Path with Maximum Probability.
Memory Usage: 30.43 MB, less than 10.03% of Python online submissions for Path with Maximum Probability.
"""
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adjMap = defaultdict(list)
        weiMap = defaultdict(int)
        for i, edge in enumerate(edges):
            a, b = edge
            adjMap[a].append(b)
            adjMap[b].append(a)
            
            weiMap[(a, b)] = succProb[i]
            weiMap[(b, a)] = succProb[i]


        maxHeap = [(-1, start_node)]
        visited = set()
        while maxHeap:
            prob, node = heapq.heappop(maxHeap)
            if node == end_node:
                return prob * -1

            visited.add(node)

            for nei in adjMap[node]:
                if nei not in visited:
                    heapq.heappush(maxHeap, (prob * weiMap[node, nei], nei))

        return 0.0