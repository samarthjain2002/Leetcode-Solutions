"""
Accepted
1032 [Hard]
Runtime: 150 ms, faster than 64.94% of Python3 online submissions for Stream of Characters.
Memory Usage: 46.81 MB, less than 40.80% of Python3 online submissions for Stream of Characters.
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False

class StreamChecker:
    def __init__(self, words: List[str]):
        self.stream = ""
        self.maxLength = 0

        self.root = TrieNode()
        for word in words:
            self.maxLength = max(self.maxLength, len(word))
            node = self.root
            for char in word[::-1]:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.endWord = True

    def query(self, letter: str) -> bool:
        self.stream += letter
        if len(self.stream) > self.maxLength:
            self.stream = self.stream[1 : ]

        node = self.root
        for char in self.stream[::-1]:
            if char in node.children:
                node = node.children[char]
                if node.endWord:
                    return True
            else:
                return False
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)