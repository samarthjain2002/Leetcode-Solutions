"""
Accepted
520 [Easy]
Runtime: 12 ms, faster than 70.32% of Java online submissions for Detect Capital.
Memory Usage: 13.50 MB, less than 13.47% of Java online submissions for Detect Capital.
"""
class Solution(object):

    @staticmethod
    def isCap(wd):
            if ord(wd[0]) >=65 and ord(wd[0])<=90:
                return True
            else:
                return False

    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        allCaps = False

        if len(word) == 1:
            return True
        elif self.isCap(word[1]):
            allCaps = True

        if self.isCap(word[0]):
            cap = True
        else:
            cap = False

        for i in range(1,len(word)):
            if allCaps == True:
                if not(self.isCap(word[i])):
                    return False
            else:
                if self.isCap(word[i]):
                    return False
            if cap == False and self.isCap(word[i]) == True:
                return False

        return True