import sys
import re

def find_numbers(line: str) -> int:
    first: int = -1
    last: int = -1
    for i in range(len(line)):
        if first < 0:
            try:
                first: int = int(line[i])
            except ValueError:
                pass
        if last < 0:
            try:
                last: int = int(line[-1 - i])
            except ValueError:
                pass
        if first > 0 and last > 0:
            break
    return int(first * 10 + last)

def find_funky_numbers(line: str) -> int:
    numbermap = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    numbers = re.compile("(?=(" + "|".join(numbermap.keys()) + "|\d{1}))")
    found_numbers = numbers.findall(line)
    first, last = found_numbers[0], found_numbers[-1]
    first = numbermap[first] if first in numbermap else int(first)
    last = numbermap[last] if last in numbermap else int(last)
    number = int(first * 10 + last)
    print(line, found_numbers, number)
    return number


if __name__ == "__main__":
    input_file = sys.argv[1]

    with open(input_file) as f:
        input = [line.strip() for line in f.readlines()]

    numbers = [find_numbers(line) for line in input]
    # print(numbers)

    result1 = sum(numbers)
    print(result1)

    numbers_again = [find_funky_numbers(line) for line in input]
    result2 = sum(numbers_again)
    print(result2)
    
    # print(find_funky_numbers("tmoneightzstdjqjncnkpkknzoneonethreefive7"))