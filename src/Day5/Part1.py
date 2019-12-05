class Part1:
    counter = 0
    numbers = list()

    def __init__(self):
        file = open("../../resource/Day5/input.txt", "r")

        line = file.read()
        self.numbers = line.split(',')
        for i in range(len(self.numbers)):
            self.numbers[i] = int(self.numbers[i])

    def calc(self, input):
        i = 0
        while True:
            one = self.numbers[i]
            parse_instruction = [int(str(one)[j]) for j in range(len(str(one)) - 1, -1, -1)]
            address_modes = []
            opcode = parse_instruction[0]

            if one == 99:
                break

            for j in parse_instruction[2:]:
                address_modes.append(j)
            while len(address_modes) < 3:
                address_modes.append(0)

            two = self.numbers[i + 1]
            three = self.numbers[i + 2]
            four = self.numbers[i + 3]

            value1 = i + 1 if address_modes[0] == 1 else two
            value2 = i + 2 if address_modes[1] == 1 else three
            value3 = i + 3 if address_modes[2] == 1 else four

            if opcode == 1:
                self.numbers[value3] = self.numbers[value1] + self.numbers[value2]
                i += 4
            elif opcode == 2:
                self.numbers[value3] = self.numbers[value1] * self.numbers[value2]
                i += 4
            elif opcode == 3:
                self.numbers[two] = input
                i += 2
            elif opcode == 4:
                print(self.numbers[two])
                i += 2

part1 = Part1()
part1.calc(1)
