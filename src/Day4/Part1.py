import re


class Part1:
    start = 231832
    end = 767346
    counter = 0

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

            self.counter += 1

        print(self.counter)


part1 = Part1()
