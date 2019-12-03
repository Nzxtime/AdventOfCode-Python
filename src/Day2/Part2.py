class Part2:
    counter = 0
    numbers = list()

    def __init__(self):
        file = open("../../resource/Day2/input.txt", "r")

        line = file.read()
        self.numbers = line.split(',')
        for i in range(len(self.numbers)):
            self.numbers[i] = int(self.numbers[i])

    def calc(self):
        for i in range(0, len(self.numbers) - 1, 4):
            one = self.numbers[i]
            two = self.numbers[i + 1]
            three = self.numbers[i + 2]
            four = self.numbers[i + 3]
            if one == 1:
                self.numbers[four] = self.numbers[two] + self.numbers[three]
            elif one == 2:
                self.numbers[four] = self.numbers[two] * self.numbers[three]
            elif one == 99:
                break


for x in range(100):
    for y in range(100):
        part2 = Part2()
        part2.numbers[1] = x
        part2.numbers[2] = y
        part2.calc()
        if part2.numbers[0] == 19690720:
            print(100 * x + y)
