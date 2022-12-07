import sys

def find_code(signal, distinct=4):
    for i in range(distinct, len(signal)):
        if len(set(signal[i-distinct:i])) == distinct:
            return i

if __name__ == "__main__":
    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    line = lines[0]
    print(find_code(line))
    print(find_code(line, 14))
