"""
Accepted
2094 [Easy]
Runtime: 27 ms, faster than 76.67% of Python3 online submissions for Finding 3-Digit Even Numbers.
Memory Usage: 18.02 MB, less than 28.25% of Python3 online submissions for Finding 3-Digit Even Numbers.
"""
# TC: O(1)
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digCount = defaultdict(int)
        for digit in digits:
            digCount[digit] += 1

        res = []
        for i in range(100, 999, 2):
            temp = [0] * 10
            for j in str(i):
                temp[int(j)] += 1

            flag = False
            for j in range(10):
                if temp[j] > digCount[j]:
                    flag = True
                    break

            if flag:
                continue
            else:
                res.append(i)
                
        return res



"""
Runtime: 2682 ms, faster than 28.12% of Python3 online submissions for Finding 3-Digit Even Numbers.
Memory Usage: 17.88 MB, less than 65.57% of Python3 online submissions for Finding 3-Digit Even Numbers.
"""
# TC: O(n^3)
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i == j or j == k or k == i:
                        continue
                    if digits[i] != 0 and digits[k] % 2 == 0:
                        num = digits[i] * 100 + digits[j] * 10 + digits[k]
                        res.add(num)
                        
        res = sorted(list(res))
        return res