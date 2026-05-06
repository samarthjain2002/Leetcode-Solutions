"""
Accepted
1861 [Medium]
Runtime: 143 ms, faster than 41.18% of Python3 online submissions for Rotating the Box.
Memory Usage: 52.05 MB, less than 91.48% of Python3 online submissions for Rotating the Box.
"""
class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # Move right
        for i in range(len(boxGrid)):
            right = len(boxGrid[0]) - 1
            for left in range(len(boxGrid[0]) - 1, -1, -1):
                if boxGrid[i][left] == '.':
                    continue
                elif boxGrid[i][left] == '*':
                    right = left - 1
                elif boxGrid[i][left] == '#':
                    boxGrid[i][left] = '.'
                    boxGrid[i][right] = '#'
                    right -= 1

        # Rotate the box
        newGrid = [['.'] * len(boxGrid) for _ in range(len(boxGrid[0]))]
        for i in range(len(boxGrid)):
            for j in range(len(boxGrid[0])):
                newGrid[j][len(boxGrid) - i - 1] = boxGrid[i][j]

        return newGrid



"""
Runtime: 1906 ms, faster than 44.09% of Python3 online submissions for Rotating the Box.
Memory Usage: 30.44 MB, less than 5.11% of Python3 online submissions for Rotating the Box.
"""
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        M, N = len(box), len(box[0])
        res = [['.' for _ in range(M)] for _ in range(N)]
        hashMap = defaultdict(list)

        for i in range(len(box)):
            count = 0
            for j, item in enumerate(box[i]):
                if item == '#':
                    count += 1
                elif item == '*':
                    res[j][abs(i - M) - 1] = item
                    if count:
                        hashMap[abs(i - M) - 1].append([count, j - 1])
                        count = 0
                if j == N - 1:
                    if count:
                        hashMap[abs(i - M) - 1].append([count, N - 1])

        for j in range(M):
            for k in range(len(hashMap[j])):
                for i in range(hashMap[j][k][1], hashMap[j][k][1] - hashMap[j][k][0], -1):
                    res[i][j] = '#'

        return res