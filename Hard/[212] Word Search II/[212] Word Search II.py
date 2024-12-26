"""
Accepted
212 [Hard]
Runtime: 7743 ms, faster than 12.13% of Python3 online submissions for Word Search II.
Memory Usage:  19.22 MB, less than 32.58% of Python3 online submissions for Word Search II.
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def buildTrie(self, word):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.endOfWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.buildTrie(word)

        res, visited = set(), set()
        def backtrack(row, col, node, string):
            if (row < 0 or row >= len(board) or 
                col < 0 or col >= len(board[0]) or 
                board[row][col] not in node.children or 
                (row, col) in visited):
                return

            visited.add((row, col))

            char = board[row][col]
            node = node.children[char]
            string += char
            if node.endOfWord:
                res.add(string)

            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for dx, dy in directions:
                backtrack(row + dx, col + dy, node, string)
            visited.remove((row, col))

        for row in range(len(board)):
            for col in range(len(board[0])):
                backtrack(row, col, root, "")

        return list(res)