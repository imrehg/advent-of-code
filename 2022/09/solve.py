import sys
import math

def moves(steps, pos_head, pos_tail):
    tail_visited = {pos_tail}
    for step in steps:
        for s in range(step[1]):
            pos_head, pos_tail = move(step[0], pos_head, pos_tail)
            # print(pos_head)
            tail_visited.add(pos_tail)

    # print(tail_visited)
    return len(tail_visited)

def move(direction, pos_head, pos_tail):
    offset: tuple[int]
    match direction:
        case 'L':
            offset = (-1, 0)
        case 'R':
            offset = (1, 0)
        case 'U':
            offset = (0, 1)
        case 'D':
            offset = (0, -1)
    
    new_pos_head = (pos_head[0] + offset[0], pos_head[1] + offset[1])
    posdiff = (new_pos_head[0] - pos_tail[0], new_pos_head[1] - pos_tail[1])
    
    new_pos_tail: tuple[int] = pos_tail
    if abs(posdiff[0]) > 1:
        new_pos_tail = (pos_tail[0] + int(math.copysign(1, posdiff[0])), pos_tail[1]+ posdiff[1])
    elif abs(posdiff[1]) > 1:
        new_pos_tail = (pos_tail[0]+posdiff[0], pos_tail[1] + int(math.copysign(1, posdiff[1])))

    # print(new_pos_head, posdiff, new_pos_tail)


    return new_pos_head, new_pos_tail

def print_pos(pos_knots):
    minx, miny, maxx, maxy = 0,0,0,0
    for pos_knot in pos_knots:
        minx = min(minx, pos_knot[0])
        maxx = max(maxx, pos_knot[0])
        miny = min(miny, pos_knot[1])
        maxy = max(maxy, pos_knot[1])

    plot = [['.' for _ in range(minx,maxx+1)] for _ in range(miny, maxy+1)]
    x = zip(reversed(range(0, len(pos_knots))), reversed(pos_knots))

    for i, knot in x:
        plot[knot[1]-miny][knot[0]-minx] = str(i) if i > 0 else 'H'

    for line in reversed(plot):
        print("".join(line))

def moves_more(steps, pos_head, knots = 10):
    pos_knot = [pos_head for _ in range(knots)]
    tail_visited = {pos_knot[-1]}
    i = 0
    for step in steps:
        i += 1
        for s in range(step[1]):
            # print(i, s,'H')
            # print(pos_knot[0], pos_knot[1])
            pos_knot[0], pos_knot[1] = move2(step[0], pos_knot[0], pos_knot[1])
            # print(pos_knot[0], pos_knot[1])
            for knot in range(2, knots):
                # print(i, s, knot)
                # print(pos_knot[knot-1], pos_knot[knot])
                pos_knot[knot-1], pos_knot[knot] = move2('X', pos_knot[knot-1], pos_knot[knot])
                # print(pos_knot[knot-1], pos_knot[knot])
                # print
                # print_pos(pos_knot)
            # print(pos_knot)
            tail_visited.add(pos_knot[-1])

    # print(pos_knot)
    # print(tail_visited)
    return len(tail_visited)

def move2(direction, pos_head, pos_tail):
    offset: tuple[int] = (0, 0)
    match direction:
        case 'L':
            offset = (-1, 0)
        case 'R':
            offset = (1, 0)
        case 'U':
            offset = (0, 1)
        case 'D':
            offset = (0, -1)
    
    new_pos_head = (pos_head[0] + offset[0], pos_head[1] + offset[1])
    posdiff = (new_pos_head[0] - pos_tail[0], new_pos_head[1] - pos_tail[1])
    
    new_pos_tail: tuple[int] = pos_tail
    if (abs(posdiff[0]) > 1) and abs(posdiff[1]) > 1:
        new_pos_tail = (pos_tail[0] + int(math.copysign(1, posdiff[0])), pos_tail[1] + int(math.copysign(1, posdiff[1])))
    elif abs(posdiff[0]) > 1:
        new_pos_tail = (pos_tail[0] + int(math.copysign(1, posdiff[0])), pos_tail[1]+ posdiff[1])
    elif abs(posdiff[1]) > 1:
        new_pos_tail = (pos_tail[0]+posdiff[0], pos_tail[1] + int(math.copysign(1, posdiff[1])))

    # print(new_pos_head, posdiff, new_pos_tail)


    return new_pos_head, new_pos_tail


if __name__ == "__main__":
    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    steps = [line.split() for line in lines]
    steps = [(x, int(y)) for x, y in steps]
    # print(steps)
    pos_head = (0, 0)
    pos_tail = (0, 0)
    x = moves(steps, pos_head, pos_tail)
    print(x)

    x = moves_more(steps, pos_head, knots=10)
    print(x)
