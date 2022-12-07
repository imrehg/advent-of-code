import sys


def contained(line):
    part1, part2 = line.split(",")
    start1, end1 = [int(num) for num in part1.split("-")]
    start2, end2 = [int(num) for num in part2.split("-")]
    return 1 if ((start1 <= start2) and (end1 >= end2)) or ((start1 >= start2) and (end1 <= end2)) else 0

def overlap(line):
    part1, part2 = line.split(",")
    start1, end1 = [int(num) for num in part1.split("-")]
    start2, end2 = [int(num) for num in part2.split("-")]
    no1 = set(range(start1, end1+1))
    no2 = set(range(start2, end2+1))
    return min(1, len(set.intersection(no1, no2)))



if __name__ == "__main__":
    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    total = 0
    for line in lines:
        total += contained(line)
    print(total)

    total = 0
    for line in lines:
        # print("line:", overlap(line))
        total += overlap(line)
    print(total)