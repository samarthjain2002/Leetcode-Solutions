"""
Accepted
166 [Medium]
Runtime: 30 ms, faster than 85.86% of Python3 online submissions for Fraction to Recurring Decimal.
Memory Usage: 18.18 MB, less than 20.36% of Python3 online submissions for Fraction to Recurring Decimal.
"""
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)

        negative = '-' if (numerator < 0) ^ (denominator < 0) else ''
        numerator, denominator = abs(numerator), abs(denominator)
            
        res = [negative + str(numerator // denominator) + '.']

        remainder = numerator % denominator
        remainders = {}

        while remainder:
            if remainder in remainders:
                res.insert(remainders[remainder], '(')
                res.append(')')
                break

            remainders[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder = remainder % denominator

        return "".join(res)