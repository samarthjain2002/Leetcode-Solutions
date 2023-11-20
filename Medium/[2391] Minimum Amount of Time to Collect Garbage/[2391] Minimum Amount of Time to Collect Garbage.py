"""
2391. Minimum Amount of Time to Collect Garbage
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
                if metal != -1 and paper != -1 and glass != -1:
                    break
            else:
                continue
            break

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