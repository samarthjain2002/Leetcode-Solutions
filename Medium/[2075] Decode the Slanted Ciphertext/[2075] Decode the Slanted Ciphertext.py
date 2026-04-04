"""
Accepted
2075 [Medium]
Runtime: 435 ms, faster than 6.49% of Python3 online submissions for Decode the Slanted Ciphertext.
Memory Usage: 40.05 MB, less than 10.39% of Python3 online submissions for Decode the Slanted Ciphertext.
"""
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        no_of_cols = math.ceil(len(encodedText) / rows)

        mat = [['$'] * no_of_cols for _ in range(rows)]
        for i in range(len(encodedText)):
            mat[i // no_of_cols][i % no_of_cols] = encodedText[i]

        originalText = []
        i = j = k = 0
        while True:
            if i == 0 and j == no_of_cols:
                break
            elif i == rows or j == no_of_cols:
                k += 1
                i, j = 0, k
                continue

            if mat[i][j] == '$':
                break

            originalText.append(mat[i][j])
            i, j = i + 1, j + 1

        return "".join(originalText).rstrip()
        