"""
Accepted
2641 [Medium]
Runtime: 164 ms, faster than 93.49% of Python3 online submissions for Convert an Cousins in Binary Tree II.
Memory Usage: 80.29 MB, less than 23.40% of Python3 online submissions for Convert an Cousins in Binary Tree II.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        siblings = defaultdict(int)

        def bfs(root):
            levelSums = []
            queue = [root]
            while queue:
                temp = []
                levelSum = 0
                for node in queue:
                    levelSum += node.val
                    if node.left and node.right:
                        siblings[node.left] = node.right.val
                        siblings[node.right] = node.left.val
                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)
                queue = temp
                levelSums.append(levelSum)
            return levelSums

        levelSums = bfs(root)

        def dfs(node, level):
            if not node:
                return

            node.val = levelSums[level] - node.val - siblings[node]

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return root