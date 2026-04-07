"""
Accepted
2069 [Medium]
Runtime: 229 ms, faster than 33.33% of Python3 online submissions for Walking Robot Simulation II.
Memory Usage: 27.17 MB, less than 6.84% of Python3 online submissions for Walking Robot Simulation II.
"""
class Robot:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.MOD = (height * 2) + ((width - 2) * 2) # Robot only walks along the perimeter, remove additional steps
        self.pos = [0, 0]
        self.dir = 1    # Directions(Clockwise): 0: North, 1: East, 2: South, 3: West

    def step(self, num) -> None:
        num = num % self.MOD
        if num == 0:    # If exactly n laps
            if self.pos == [0, 0]:
                self.dir = 2    # Face south if you have never moved and complete n laps

        def stepRight(num):
            if self.pos[0] + num > self.width - 1:
                num = num - (self.width - 1 - self.pos[0])
                self.pos[0] = self.width - 1
                self.dir = 0
                stepUp(num)
            else:
                self.pos[0] += num
                
        def stepUp(num):
            if self.pos[1] + num > self.height - 1:
                num = num - (self.height - 1 - self.pos[1])
                self.pos[1] = self.height - 1
                self.dir = 3
                stepLeft(num)
            else:
                self.pos[1] += num
                
        def stepLeft(num):
            if self.pos[0] - num < 0:
                num = num - self.pos[0]
                self.pos[0] = 0
                self.dir = 2
                stepDown(num)
            else:
                self.pos[0] -= num
                
        def stepDown(num):
            if self.pos[1] - num < 0:
                num = num - self.pos[1]
                self.pos[1] = 0
                self.dir = 1
                stepRight(num)
            else:
                self.pos[1] -= num
        
        if self.dir == 1:
            stepRight(num)
        elif self.dir == 0:
            stepUp(num)
        elif self.dir == 3:
            stepLeft(num)
        else:
            stepDown(num)

    def getPos(self):
        return self.pos        

    def getDir(self) -> str:
        if self.dir == 1:
            return "East"
        elif self.dir == 0:
            return "North"
        elif self.dir == 3:
            return "West"
        else:
            return "South"
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()