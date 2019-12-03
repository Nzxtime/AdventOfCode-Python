import math


class Part2:
    totalMass = 0

    def __init__(self):
        file = open("../../resource/Day1/input.txt", "r")

        for line in file:
            Part2.calc_fuel(self, int(line))

        print(self.totalMass)

    def calc_fuel(self, a):
        mass = math.floor(a / 3) - 2
        if mass <= 0:
            return 0
        else:
            self.totalMass += mass
            return self.calc_fuel(mass)


part2 = Part2()
