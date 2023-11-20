"""
Accepted
2391 [Medium]
Runtime: 1111 ms, faster than 14.04% of Python3 online submissions for Minimum Amount of Time to Collect Garbage.
Memory Usage: 39.51 MB, less than 14.71% of Python3 online submissions for Minimum Amount of Time to Collect Garbage.
"""
#https://chat.openai.com/share/8c0424de-dee8-477e-9314-fa6ccea8b3e2
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:

        metal = paper = glass = -1
        for i in range(len(garbage)-1,-1,-1):
            for j in range(0,len(garbage[i])):
                if garbage[i][j] == 'M' and metal == -1:
                    metal = i
                if garbage[i][j] == 'P' and paper == -1:
                    paper = i
                if garbage[i][j] == 'G' and glass == -1:
                    glass = i
                if metal != -1 and paper != -1 and glass != -1:     #Your condition to exit both loops
                    break       #Breaks the inner loop
            else:       #This will only execute if the inner loop completes without hitting the 'break' statement
                continue
            break       #Breaks the outer loop

        count  = 0

        for i in range(0,len(garbage)):
            for j in range(0,len(garbage[i])):
                if garbage[i][j] == 'M' and i < metal + 1:
                    count += 1
                if garbage[i][j] == 'P' and i < paper + 1:
                    count += 1
                if garbage[i][j] == 'G' and i < glass + 1:
                    count += 1
            if i < metal:
                count += travel[i]
            if i < paper:
                count += travel[i]
            if i < glass:
                count += travel[i]

        return count