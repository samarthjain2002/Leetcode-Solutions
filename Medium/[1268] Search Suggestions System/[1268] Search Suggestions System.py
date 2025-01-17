"""
Accepted
1268 [Medium]
Runtime: 4 ms, faster than 90.88% of Python3 online submissions for Search Suggestions System.
Memory Usage: 20.50 MB, less than 69.45% of Python3 online submissions for Search Suggestions System.
"""
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        res = []
        left, right = 0, len(products) - 1
        for i, char in enumerate(searchWord):
            while left <= right and (len(products[left]) <= i or products[left][i] != char):
                left += 1
            while left <= right and (len(products[right]) <= i or products[right][i] != char):
                right -= 1

            res.append([])
            for j in range(min(3, right - left + 1)):
                res[-1].append(products[left + j])
        return res



"""
Runtime: 295 ms, faster than 19.95% of Python3 online submissions for Search Suggestions System.
Memory Usage: 23.74 MB, less than 19.65% of Python3 online submissions for Search Suggestions System.
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self, product):
        node = self
        for char in product:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.endOfWord = True

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()
        for product in sorted(products):
            root.addWord(product)

        def dfs(node, path, suggestions):
            if len(suggestions) == 3:
                return
            if node.endOfWord:
                suggestions.append("".join(path))

            for char in sorted(node.children.keys()):
                path.append(char)
                dfs(node.children[char], path, suggestions)
                path.pop()

        res = []
        prefix = ""
        node = root
        for char in searchWord:
            prefix += char
            if char in node.children:
                node = node.children[char]
                suggestions = []
                dfs(node, list(prefix), suggestions)
                res.append(suggestions)
            else:
                while len(res) < len(searchWord):
                    res.append([])
                break

        return res