"""
Accepted
1396 [Medium]
Runtime: 34 ms, faster than 18.95% of Python3 online submissions for Design Underground System.
Memory Usage: 30.75 MB, less than 8.99% of Python3 online submissions for Design Underground System.
"""
class UndergroundSystem:
    def __init__(self):
        self.averageTimes = {}
        self.checkInTimes = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInTimes[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startingStation = self.checkInTimes[id][0]
        timeTaken = t - self.checkInTimes[id][1]

        average = count = 0
        if (startingStation, stationName) in self.averageTimes:
            average, count = self.averageTimes[(startingStation, stationName)]

        newAvg = ((average * count) + timeTaken) / (count + 1)
        self.averageTimes[(startingStation, stationName)] = [newAvg, count + 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.averageTimes[(startStation, endStation)][0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)