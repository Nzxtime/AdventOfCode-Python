class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'x[{}]:y[{}]'.format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return self.x + self.y


class Part1:
    ma = dict()
    mb = dict()
    intersections = list()

    def __init__(self):
        file = open("../../resource/Day3/input.txt", "r")
        line_a = next(file)
        line_b = next(file)

        self.ma = Part1.do_path(self, line_a, self.ma)
        self.mb = Part1.do_path(self, line_b, self.mb)

        # Get the intersection
        self.intersections = [k for k in self.ma if k in self.mb]
        self.get_nearest_intersection()

    def do_path(self, line, dictionary):
        x = 0
        y = 0
        counter = 0
        instructions = line.split(",")
        for instruction in instructions:
            direction = instruction[:1]
            moves = int(instruction[1:])

            if direction == 'R':
                for i in range(moves):
                    x += 1
                    dictionary[Point(x, y)] = counter
                    counter += 1
            elif direction == 'L':
                for i in range(moves):
                    x -= 1
                    dictionary[Point(x, y)] = counter
                    counter += 1
            elif direction == 'U':
                for i in range(moves):
                    y += 1
                    dictionary[Point(x, y)] = counter
                    counter += 1
            elif direction == 'D':
                for i in range(moves):
                    y -= 1
                    dictionary[Point(x, y)] = counter
                    counter += 1
        return dictionary

    def get_nearest_intersection(self):
        distance = float('inf')
        for intersection in self.intersections:
            temp_distance = abs(intersection.x) + abs(intersection.y)
            if temp_distance < distance:
                distance = temp_distance
        print(distance)


part1 = Part1()
