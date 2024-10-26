"""
Accepted
2458 [Hard]
Runtime: 320 ms, faster than 93.33% of Python3 online submissions for Height of Binary Tree After Subtree Removal Queries.
Memory Usage: 62.50 MB, less than 41.28% of Python3 online submissions for Height of Binary Tree After Subtree Removal Queries.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        heights = defaultdict(int)
        def dfs(node):
            if not node:
                return -1
            
            heights[node.val] = 1 + max(dfs(node.left), dfs(node.right))
            return heights[node.val]

        dfs(root)
        
        def bfs(root):
            nonlocal answers
            queue = [root]
            level = -1
            while queue:
                level += 1
                temp = []
                max2Heights = [level - 1, -1]
                for node in queue:
                    if heights[node.val] + level > max2Heights[0]:
                        max2Heights[1] = max2Heights[0]
                        max2Heights[0] = heights[node.val] + level
                    elif heights[node.val] + level > max2Heights[1]:
                        max2Heights[1] = heights[node.val] + level

                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)

                for node in queue:
                    answers[node.val] = [level, max2Heights]

                queue = temp

        answers = {}
        bfs(root)

        res = []
        for query in queries:
            if answers[query][0] + heights[query] == answers[query][1][0]:
                res.append(answers[query][1][1])
            else:
                res.append(answers[query][1][0])

        return res