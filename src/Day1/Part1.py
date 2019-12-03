import math

mass = 0
file = open("../../resource/Day1/input.txt", "r")

for line in file:
    mass += (math.floor(int(line) / 3) - 2)

print(mass)
