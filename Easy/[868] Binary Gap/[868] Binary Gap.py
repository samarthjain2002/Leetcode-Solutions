"""
Accepted
868 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Binary Gap.
Memory Usage: 19.43 MB, less than 31.55% of Python3 online submissions for Binary Gap.
"""
class Solution:
    def binaryGap(self, n: int) -> int:
        b = bin(n)[2 : ]
	pos = 0
	res = 0
	for i in range(len(b)):
	    if b[i] == '1':
		res = max(res, i - pos)
		pos = i
	return res