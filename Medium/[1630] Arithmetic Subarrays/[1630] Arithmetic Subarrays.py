"""
Accepted
1630 [Medium]
Runtime: 198 ms, faster than 25.84% of Python3 online submissions for Arithmetic Subarrays.
Memory Usage: 16.56 MB, less than 39.64% of Python3 online submissions for Arithmetic Subarrays.
"""
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        for i in range(0,len(l)):
            subArray = []
            for j in range(l[i],r[i]+1):
                subArray.append(nums[j])

            subArray.sort()

            diff = subArray[1] - subArray[0]
            for j in range(1,len(subArray)):
                if subArray[j] - subArray[j-1] != diff:
                    answer.append(False)
                    break   #Breaks the inner loop
            else:   #This will only execute if the inner loop completes without hitting the 'break' statement
                answer.append(True)
            
        return answer