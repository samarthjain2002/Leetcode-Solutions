"""
Accepted
2434 [Medium]
Runtime: 2391 ms, faster than 5.34% of Python3 online submissions for Using a Robot to Print the Lexicographically Smallest String.
Memory Usage: 20.39 MB, less than 87.79% of Python3 online submissions for Using a Robot to Print the Lexicographically Smallest String.
"""
class Solution:
    def robotWithString(self, s: str) -> str:
        charFreq = Counter(s)

        def smallest(cur):
            for char, freq in charFreq.items():
                if char < cur and freq:
                    return False
            return True

        robotStack = []
        res = ""
        for i in range(len(s)):
            # Check if there exists a smaller character ahead (to the right)
            if not smallest(s[i]):
                robotStack.append(s[i])
                charFreq[s[i]] -= 1
            # If there is no smaller character ahead
            else:
                # Current character is the smallest character, so add it to result
                res += s[i]
                charFreq[s[i]] -= 1
                
                # Check for every character at the top of the stack
                while robotStack:
                    # If the top of the stack is smaller than all the characters ahead (to the right)
                    if smallest(robotStack[-1]):
                        res += robotStack.pop()
                    else:
                        break
                    
        return res



"""
Runtime: 2746 ms, faster than 5.34% of Python3 online submissions for Using a Robot to Print the Lexicographically Smallest String.
Memory Usage: 20.40 MB, less than 82.06% of Python3 online submissions for Using a Robot to Print the Lexicographically Smallest String.
"""
class Solution:
    def robotWithString(self, s: str) -> str:
        charFreq = Counter(s)

        robotStack = []
        res = ""
        for i in range(len(s)):
            # Check if there exists a smaller character ahead (to the right)
            for char, freq in charFreq.items():
                if char < s[i] and freq:
                    robotStack.append(s[i])
                    charFreq[s[i]] -= 1
                    break
            # If the for completes without hitting break (no smaller character ahead)
            else:
                # Current character is the smallest character, so add it to result
                res += s[i]
                charFreq[s[i]] -= 1
                
                # Check for every character at the top of the stack
                while robotStack:
                    # If the top of the stack is smaller than all the characters ahead (to the right)
                    for char, freq in charFreq.items():
                        if char < robotStack[-1] and freq:
                            break
                    else:
                        res += robotStack.pop()
                        continue
                    break
                    
        return res