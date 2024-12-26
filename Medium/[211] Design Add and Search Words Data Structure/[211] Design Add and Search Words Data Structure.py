"""
Accepted
211 [Medium]
Runtime: 1302 ms, faster than 45.04% of Python3 online submissions for Design Add and Search Words Data Structure.
Memory Usage:  65.46 MB, less than 27.83% of Python3 online submissions for Design Add and Search Words Data Structure.
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        def backtrack(j, root):
            node = root
            for i in range(j, len(word)):
                char = word[i]
                if char == '.':
                    for child in node.children.values():
                        if backtrack(i + 1, child):
                            return True
                    return False
                else:
                    if char not in node.children:
                        return False
                    node = node.children[char]
            return node.endOfWord

        return backtrack(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)