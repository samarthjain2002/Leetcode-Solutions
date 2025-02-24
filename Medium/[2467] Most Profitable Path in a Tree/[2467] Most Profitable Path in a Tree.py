"""
Accepted
2467 [Medium]
Runtime: 217 ms, faster than 69.49% of Python3 online submissions for Most Profitable Path in a Tree.
Memory Usage: 72.11 MB, less than 15.93% of Python3 online submissions for Most Profitable Path in a Tree.
"""
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # Create adjacency map (tree)
        adjMap = defaultdict(list)
        for edge in edges:
            a, b = edge[0], edge[1]
            adjMap[a].append(b)
            adjMap[b].append(a)

        # Bob's path and time
        bobTime = {bob: 0}
        visited = set([bob])
        def BobBacktrack(node, time):
            if node == 0:
                return True

            for n in adjMap[node]:
                if n not in visited:
                    visited.add(n)
                    bobTime[n] = time + 1
                    if BobBacktrack(n, time + 1):
                        return True
                    del bobTime[n]
            return False

        BobBacktrack(bob, 0)

        # Alice's paths
        res = -float("inf")
        queue = deque([(0, amount[0])])
        visited = set([0])
        time = 0
        while queue:
            time += 1

            for i in range(len(queue)):
                node, count = queue.popleft()
                leaf = True

                for n in adjMap[node]:
                    if n not in visited:
                        leaf = False
                        visited.add(n)

                        if n in bobTime:
                            if time == bobTime[n]:
                                queue.append((n, count + amount[n] // 2))
                                continue
                            elif time > bobTime[n]:
                                queue.append((n, count))
                                continue
                        queue.append((n, count + amount[n]))

                if leaf:
                    res = max(res, count)
                    
        return res