"""
Accepted
3093 [Hard]
Runtime: 1095 ms, faster than 76.73% of Python3 online submissions for Longest Common Suffix Queries.
Memory Usage: 165.35 MB, less than 69.81% of Python3 online submissions for Longest Common Suffix Queries.
"""
# Trie Solution
class TrieNode:
    def __init__(self, ans):
        self.children = {}
        self.ans = ans


class Trie:
    def __init__(self, wordsContainer, ans):
        self.root = TrieNode(ans)
        self.wordsContainer = wordsContainer

    def insert(self, i, word):
        node = self.root
        for char in reversed(word):
            if char not in node.children:
                node.children[char] = TrieNode(i)
            else:
                if len(word) <= len(self.wordsContainer[node.children[char].ans]):
                    node.children[char].ans = i
            node = node.children[char]

    def query(self, word):
        node = self.root
        res = node.ans
        for char in reversed(word):
            if char not in node.children:
                break
            res = node.children[char].ans
            node = node.children[char]
        return res


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        default = 0
        for i, word in enumerate(wordsContainer):
            if len(word) < len(wordsContainer[default]):
                default = i

        trie = Trie(wordsContainer, default)

        for i in reversed(range(len(wordsContainer))):
            word = wordsContainer[i]
            trie.insert(i, word)
        
        res = []
        for word in wordsQuery:
            ans = trie.query(word)
            res.append(ans)
        return res