"""
Accepted
401 [Easy]
Runtime: 3 ms, faster than 34.33% of Python3 online submissions for Binary Watch.
Memory Usage: 17.93 MB, less than 25.58% of Python3 online submissions for Binary Watch.
"""
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn > 8:
            return []

        res = []
        for hr in range(12):
            for mins in range(60):
                if bin(hr).count('1') + bin(mins).count('1') == turnedOn:
                    if mins < 10:
                        mins = "0" + str(mins)
                    res.append(f"{hr}:{mins}")
        return res



"""
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Binary Watch.
Memory Usage: 17.88 MB, less than 43.04% of Python3 online submissions for Binary Watch.
"""
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn > 8:
            return []

        hourBit = defaultdict(list)
        minBit = defaultdict(list)
        for i in range(60):
            if i < 12:
                hourBit[bin(i).count('1')].append(f"{i}")

            if i < 10:
                minBit[bin(i).count('1')].append(f"0{i}")
            else:
                minBit[bin(i).count('1')].append(f"{i}")


        res = []
        for i in range(min(turnedOn + 1, 4)):
            if turnedOn - i > 5:
                continue

            for hr in hourBit[i]:
                string = f"{hr}:"

                for mins in minBit[turnedOn - i]:
                    string += mins
                    res.append(string)
                    string = string[ : -1 * len(mins)]

        return res