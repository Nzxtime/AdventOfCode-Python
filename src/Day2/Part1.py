class Part1:
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
            if (one == 1):
                self.numbers[four] = self.numbers[two] + self.numbers[three]
            elif (one == 2):
                self.numbers[four] = self.numbers[two] * self.numbers[three]
            elif (one == 99):
                break

        print(self.numbers[0])


part1 = Part1()
part1.numbers[1] = 12
part1.numbers[2] = 2
part1.calc()
