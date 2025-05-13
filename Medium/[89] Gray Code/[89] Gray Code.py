"""
Accepted
89 [Medium]
Runtime: 223 ms, faster than 5.02% of Python3 online submissions for Gray Code.
Memory Usage: 47.38 MB, less than 5.32% of Python3 online submissions for Gray Code.
"""
class Solution:
    def grayCode(self, n: int) -> List[int]:
        def binary_to_integer(s):
            num = 0
            for i, bit in enumerate(s[::-1]):
                if bit == '1':
                    num += 2**i
            return num

        def differ_by_one(code1, code2):
            flag = False
            for i in range(n):
                if code1[i] != code2[i]:
                    if flag == True:
                        return False
                    else:
                        flag = True
            return flag

        res = [0]
        visited = set(['0' * n])
        def backtrack(index, code):
            if index == 2**n:
                if differ_by_one(code, '0' * n):
                    return True
                else:
                    return False

            for i in range(n):
                new_bit = '1' if code[i] == '0' else '0'
                new_code = code[ : i] + new_bit + code[i + 1 : ]
                if new_code in visited:
                    continue

                res.append(binary_to_integer(new_code))
                visited.add(new_code)
                if backtrack(index + 1, new_code):
                    return True
                visited.remove(new_code)
                res.pop()


        backtrack(1, '0' * n)
        return res