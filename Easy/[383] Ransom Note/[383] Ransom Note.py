"""
Accepted
383 [Easy]
Runtime: 65 ms, faster than 30.20% of Python3 online submissions for Ransom Note.
Memory Usage: 16.60 MB, less than 96.64% of Python3 online submissions for Ransom Note.
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMap = defaultdict(int)
        for char in magazine:
            hashMap[char] += 1
        
        for char in ransomNote:
            if hashMap[char] > 0:
                hashMap[char] -= 1
            else:
                return False
        return True