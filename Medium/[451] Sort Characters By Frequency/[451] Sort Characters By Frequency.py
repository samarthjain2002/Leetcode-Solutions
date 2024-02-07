"""
Accepted
451 [Medium]
Runtime: 51 ms, faster than 45.89% of Python3 online submissions for Sort Characters By Frequency.
Memory Usage:  17.69 MB, less than 93.07% of Python3 online submissions for Sort Characters By Frequency.
"""
class Solution:
    def frequencySort(self, s: str) -> str:
        freqList = [[0, char] for char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']

        for char in s:
            if 97 <= ord(char) <= 122:
                freqList[ord(char) - ord('a')][0] += 1
            elif 65 <= ord(char) <= 90:
                freqList[ord(char) - ord('A') + 26][0] += 1
            else:
                freqList[int(char) + 52][0] += 1
        freqList.sort()

        s = ""
        for freq in range(61, -1, -1):  #26[a-z] 26[A-Z] 10[0-9]
            s += freqList[freq][1] * freqList[freq][0]

        return s