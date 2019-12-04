import re


class Part2:
    start = 231832
    end = 767346
    counter = 0
    numbers = list()

    def __init__(self):
        for x in range(self.start, self.end):
            breaker = False
            if re.search("(1{2}|2{2}|3{2}|4{2}|5{2}|6{2}|7{2}|8{2}|9{2})", str(x)) is None:
                continue
            digits = [int(x) for x in str(x)]
            for i in range(1, len(digits)):
                if digits[i - 1] > digits[i]:
                    breaker = True
                    break

            if breaker:
                continue

            self.numbers.append(x)

        self.filter()
        print(self.counter)

    def filter(self):
        for number in self.numbers:
            if 2 in [str(number).count(d) for d in str(number)]:
                self.counter += 1


part2 = Part2()
