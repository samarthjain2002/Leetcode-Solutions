"""
Accepted
8 [Medium]
Runtime: 28 ms, faster than 96.63% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 16.79 MB, less than 21.00% of Python3 online submissions for String to Integer (atoi).
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        negative = False
        for i, char in enumerate(s):
            if char == ' ':
                continue
            elif char == '-':
                negative = True
                s = s[i + 1 : ]
            elif char == '+':
                s = s[i + 1 : ]
            else:
                s = s[i : ]
            break

        def check(negative, res):
            print(res)
            maxi, mini = "2147483647", "2147483648"
            if res:
                if negative:
                    if len(res) > 10:
                        return -2147483648
                    elif len(res) < 10:
                        return -1 * int(res)
                    else:
                        for i, char in enumerate(mini):
                            if res[i] > char:
                                return -2147483648
                            elif res[i] == char:
                                pass
                            else:
                                break
                    return -1 * int(res)
                else:
                    if len(res) > 10:
                        return 2147483647
                    elif len(res) < 10:
                        return int(res)
                    else:
                        for i, char in enumerate(maxi):
                            if res[i] > char:
                                return 2147483647
                            elif res[i] == char:
                                pass
                            else:
                                break
                    return int(res)
            else:
                return 0

        nonZeroDigitFound = False
        res = ""
        for char in s:
            if nonZeroDigitFound:
                if not char.isdigit():
                    return check(negative, res)
                else:
                    res += char
            elif char.isdigit():
                if char == '0':
                    continue
                res += char
                nonZeroDigitFound = True
            else:
                return 0

        return check(negative, res)