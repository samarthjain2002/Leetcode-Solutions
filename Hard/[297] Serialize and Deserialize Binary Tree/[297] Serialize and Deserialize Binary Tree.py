"""
Accepted
297 [Hard]
Runtime: 80 ms, faster than 70.86% of Python3 online submissions for Serialize and Deserialize Binary Tree.
Memory Usage: 21.50 MB, less than 14.98% of Python3 online submissions for Serialize and Deserialize Binary Tree.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return

            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(',')
        self.index = 0

        def dfs():
            if nodes[self.index] == 'N':
                self.index += 1
                return None

            node = TreeNode(int(nodes[self.index]))
            self.index += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))