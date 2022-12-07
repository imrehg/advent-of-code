import sys
import re
def crane(crates, moves):
    crate_numbers = crates[-1].split()
    ncrates = len(crate_numbers)
    hold = {i: '' for i in range(1, ncrates+1)}

    for line in crates[-2::-1]:
        for c in range(1, ncrates+1):
            index = ((c-1) * 4)+1
            if (value := line[index]) != " ":
                hold[c] += value

    print(hold)
    for move in moves:
        inst = re.match(r'^move (?P<move>\d+) from (?P<from>\d+) to (?P<to>\d+)$', move)
        c_to = int(inst.group('to'))
        c_from = int(inst.group('from'))
        c_num = int(inst.group('move'))
        hold[c_to] += hold[c_from][-1:-1 * c_num-1:-1]
        hold[c_from] = hold[c_from][0:-1 * c_num]
    
    res = ''
    for i in range(1, ncrates+1):
        res += hold[i][-1]
    return(res)

def crane9001(crates, moves):
    crate_numbers = crates[-1].split()
    ncrates = len(crate_numbers)
    hold = {i: '' for i in range(1, ncrates+1)}

    for line in crates[-2::-1]:
        for c in range(1, ncrates+1):
            index = ((c-1) * 4)+1
            if (value := line[index]) != " ":
                hold[c] += value

    print(hold)
    for move in moves:
        inst = re.match(r'^move (?P<move>\d+) from (?P<from>\d+) to (?P<to>\d+)$', move)
        c_to = int(inst.group('to'))
        c_from = int(inst.group('from'))
        c_num = int(inst.group('move'))
        # hold[c_to] += hold[c_from][-1:-1 * c_num-1:-1]
        hold[c_to] += hold[c_from][-1 * c_num:]
        hold[c_from] = hold[c_from][0:-1 * c_num]
        print(hold)
    
    res = ''
    for i in range(1, ncrates+1):
        res += hold[i][-1]
    return(res)

if __name__ == "__main__":
    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        lines = [line.replace("\n", "") for line in f.readlines()]

    crates = []
    moves = []
    move_line = False
    for line in lines:
        if move_line:
            moves.append(line)
        elif line == '':
            move_line = True
        else:
            crates.append(line)
    print(crane(crates, moves))
    print(crane9001(crates, moves))