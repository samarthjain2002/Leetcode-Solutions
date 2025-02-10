# Leetcode-Solutions

This repository contains my personal solutions to various LeetCode problems. The solutions are categorized based on difficulty levels: **Easy**, **Medium**, and **Hard**. Each problem's solution is stored in a separate file with the naming convention `[problemNo] ProblemName.py`.

## 📂 Repository Structure
```
Leetcode-Solutions/
│── Easy/
│── Medium/
│── Hard/
│── Badges/
│── Database/
```
- **Easy/**: Contains solutions to Easy-level LeetCode problems.
- **Medium/**: Contains solutions to Medium-level LeetCode problems.
- **Hard/**: Contains solutions to Hard-level LeetCode problems.
- **Badges/**: Stores any achievement or progress-related images.
- **Database/**: Reserved for database-related problems or scripts.

## 📝 Solution Format
Each solution file follows the format:
```python
"""
Accepted
[Problem Number] [Difficulty]
Runtime: XX ms, faster than XX% of Python3 online submissions for [Problem Name].
Memory Usage: XX MB, less than XX% of Python3 online submissions for [Problem Name].
"""
class Solution:
    def function_name(self, params):
        # Solution implementation
        pass
```
### Example:
File: `[127] Word Ladder.py`
```python
"""
Accepted
127 [Hard]
Runtime: 53 ms, faster than 88.73% of Python3 online submissions for Word Ladder.
Memory Usage: 20.87 MB, less than 29.18% of Python3 online submissions for Word Ladder.
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        adjMap = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                # Ex: "hit" -> "?it", "h?t", "hi?"
                # But hit is appended to all these patterns
                pattern = word[ : i] + "?" + word[i + 1 : ]
                adjMap[pattern].append(word)

        queue = deque([beginWord])
        visited = set([beginWord])
        res = 1
        # Breadth-First Search
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[ : i] + "?" + word[i + 1 : ]
                    for neighbor in adjMap[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
            res += 1
        return 0
```

## ⚡ Usage
- Clone the repository:
  ```sh
  git clone https://github.com/yourusername/Leetcode-Solutions.git
  ```
- Navigate to the desired difficulty folder.
- Run the Python files in your local environment to test solutions.

## 🚀 Future Enhancements
- Add problem descriptions and explanations for each solution.
- Implement a web-based interface to browse solutions.
- Automate the performance tracking of solutions.

## 📜 Disclaimer
These solutions are for personal reference and learning purposes. They may not be the most optimized solutions but can be used to understand different problem-solving approaches.

Happy Coding! 🚀

