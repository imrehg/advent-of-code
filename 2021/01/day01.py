import sys


def count_increase(data):
    count = 0
    for i, reading in enumerate(data[:-1]):
        count += 1 if data[i + 1] > reading else 0
    return count


def count_sliding_window(data):
    count = 0
    for i, _ in enumerate(data[:-3]):
        first_window = sum(data[i : i + 3])
        second_window = sum(data[i + 1 : i + 4])
        count += 1 if second_window > first_window else 0
    return count


if __name__ == "__main__":
    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        readings = [int(row.strip()) for row in f.readlines()]

    result1 = count_increase(readings)
    print(result1)

    result2 = count_sliding_window(readings)
    print(result2)
