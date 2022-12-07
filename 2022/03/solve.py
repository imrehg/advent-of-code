import sys

def priority(items):
    size = len(items) // 2
    part1, part2 = items[0:size], items[size:]
    items1, items2 = set(part1), set(part2)
    suspect = set.intersection(items1, items2).pop()
    step1 = ord(suspect)
    offset = 96 if step1 >= 97 else (64-26)
    return(step1-offset)

def badge(lines):
    part1, part2, part3 = set(lines[0]), set(lines[1]), set(lines[2])
    badge = set.intersection(part1, part2, part3).pop()
    step1 = ord(badge)
    offset = 96 if step1 >= 97 else (64-26)
    return(step1-offset)



if __name__ == "__main__":
    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    total = 0
    for line in lines:
        total += priority(line)
    print(total)

    total = 0
    for i in range(0, len(lines), 3):
        total += badge(lines[i:i+3])
    print(total)
