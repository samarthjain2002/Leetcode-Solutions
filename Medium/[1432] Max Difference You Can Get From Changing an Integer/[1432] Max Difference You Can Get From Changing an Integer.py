"""
Accepted
1432 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Max Difference You Can Get From Changing an Integer.
Memory Usage: 17.94 MB, less than 15.31% of Python3 online submissions for Max Difference You Can Get From Changing an Integer.
"""
class Solution:
    def maxDiff(self, num: int) -> int:
        number = str(num)
        change = ''
        for dig in number:
            if dig != '9':
                change = dig
                break
                
        maximum = []
        for dig in number:
            if dig == change:
                maximum.append('9')
            else:
                maximum.append(dig)


        if number[0] != '1':
            change = number[0]
        else:
            change = ''
            for dig in number:
                if dig != number[0] and dig != '0':
                    change = dig
                    break

        minimum = []
        for dig in number:
            if dig == change:
                if number[0] == '1':
                    minimum.append('0')
                else:
                    minimum.append('1')
            else:
                minimum.append(dig)

        return int("".join(maximum)) - int("".join(minimum))