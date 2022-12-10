import sys
import math

def cycles(inst):
    values = [1]
    for item in inst:
        values.append(values[-1])
        if item[0] == 'addx':
            values.append(values[-1] + int(item[1]))
    return values

def run_instructions(inst):
    values = cycles(inst)
    return sum([v1 * v2 for v1, v2 in zip(values[19::40], range(20, len(values), 40))])

def crt(inst):
    values = cycles(inst)
    screen = ''
    for i, value in enumerate(values):
        screen += "#" if value -1 <= (i % 40) <= value +1 else "."
    for i in range(0, len(screen), 40):
        print(screen[i:i+40])


if __name__ == "__main__":
    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    
    instructions = [line.split() for line in lines]
    x = run_instructions(instructions) 
    print(x)

    crt(instructions)