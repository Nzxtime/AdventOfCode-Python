class Part1:
    field = []

    def __init__(self):
        file = open("../../resource/Day3/input.txt", "r")
        field = [['.' for x in range(1000)] for y in range(1000)]
        print(field)
        for line in file:
            instructions = list()
            self.instructions = line.split(',')


part1 = Part1()
