import sys


def navigate1(steps):
    position = [0, 0]
    for command, units in steps:
        if command == "forward":
            position[0] += units
        elif command == "down":
            position[1] += units
        elif command == "up":
            position[1] -= units
    return position


def navigate2(steps):
    position, aim = [0, 0], 0
    for command, units in steps:
        if command == "forward":
            position[0] += units
            position[1] += units * aim
        elif command == "down":
            aim += units
        elif command == "up":
            aim -= units
    return position


if __name__ == "__main__":
    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        steps = []
        for row in f.readlines():
            r = row.strip().split(" ")
            steps += [(r[0], int(r[1]))]

    endpoint = navigate1(steps)
    result1 = endpoint[0] * endpoint[1]
    print(result1)

    endpoint2 = navigate2(steps)
    result2 = endpoint2[0] * endpoint2[1]
    print(result2)
