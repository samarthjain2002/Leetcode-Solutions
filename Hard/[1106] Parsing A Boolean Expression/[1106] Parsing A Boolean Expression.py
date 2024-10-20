"""
Accepted
1106 [Hard]
Runtime: 11 ms, faster than 100.00% of Python3 online submissions for Parsing A Boolean Expression.
Memory Usage: 17.02 MB, less than 8.08% of Python3 online submissions for Parsing A Boolean Expression.
"""
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        N = len(expression)
        
        def parse_and(i):
            res = True
            while expression[i] != ')' and i < N:
                if expression[i] == 'f':
                    res = False
                    i += 1
                elif expression[i] == 't':
                    i += 1
                elif expression[i] == ',':
                    i += 1
                else:
                    if expression[i] == '&':
                        boolean, i = parse_and(i + 2)
                        res = res and boolean
                        i += 1
                    elif expression[i] == '|':
                        boolean, i = parse_or(i + 2)
                        res = res and boolean
                        i += 1
                    elif expression[i] == '!':
                        boolean, i = parse_not(i + 2)
                        res = res and boolean
                        i += 1
            return res, i
        
        def parse_or(i):
            res = False
            while expression[i] != ')' and i < N:
                if expression[i] == 'f':
                    i += 1
                elif expression[i] == 't':
                    res = res or True
                    i += 1
                elif expression[i] == ',':
                    i += 1
                else:
                    if expression[i] == '&':
                        boolean, i = parse_and(i + 2)
                        res = res or boolean
                        i += 1
                    elif expression[i] == '|':
                        boolean, i = parse_or(i + 2)
                        res = res or boolean
                        i += 1
                    elif expression[i] == '!':
                        boolean, i = parse_not(i + 2)
                        res = res or boolean
                        i += 1
            return res, i
        
        def parse_not(i):
            if expression[i] == 'f':
                return True, i + 1
            elif expression[i] == 't':
                return False, i + 1
            else:
                if expression[i] == '&':
                    boolean, i = parse_and(i + 2)
                    return not boolean, i + 1
                elif expression[i] == '|':
                    boolean, i = parse_or(i + 2)
                    return not boolean, i + 1
                elif expression[i] == '!':
                    boolean, i = parse_not(i + 2)
                    return not boolean, i + 1
                
            
        if expression[0] == '&':
            res, i = parse_and(2)
            return res
        elif expression[0] == '|':
            res, i = parse_or(2)
            return res
        elif expression[0] == '!':
            res, i = parse_not(2)
            return res
        else:
            return True if expression[0] == 't' else False