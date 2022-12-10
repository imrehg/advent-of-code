import sys
import math

def visibility(mapped):
    w, h = len(mapped[0]), len(mapped)
    count = 0
    totals = 0
    for x in range(0, w):
        for y in range(0, h):
            totals +=1
            if x == 0 or y == 0 or x == w-1 or y == h -1:
                count += 1
            else:
                height = int(mapped[y][x])
                visible = (
                    not any([int(mapped[y][i]) >= height for i in range(0, x)]) 
                    or 
                    not any([int(mapped[y][i]) >= height for i in range(x+1, w)]) 
                    or
                    not any([int(mapped[i][x]) >= height for i in range(0, y)])
                    or
                    not any([int(mapped[i][x]) >= height for i in range(y+1, w)])
                )
                count += 1 if visible else 0


    return count

def scenic(mapped):
    w, h = len(mapped[0]), len(mapped)
    max_scenic = 0

    for y in range(0, h):
        for x in range(0, w):
            height = int(mapped[y][x])
            score = 1
            # print(x, y, height)

            scores = []
            count = 0
            for c in range(y-1, -1, -1):
                count += 1
                if int(mapped[c][x]) >= height:
                    break
            scores.append(count)

            count = 0
            for c in range(x-1, -1, -1):
                count += 1
                if int(mapped[y][c]) >= height:
                    break
            scores.append(count)

            count = 0
            for c in range(y+1, h):
                count += 1
                if int(mapped[c][x]) >= height:
                    break
            scores.append(count)

            count = 0
            for c in range(x+1, w):
                count += 1
                if int(mapped[y][c]) >= height:
                    break
            scores.append(count)
            score = math.prod(scores)

            # print(scores)


            max_scenic = max(max_scenic, score)

    return max_scenic

if __name__ == "__main__":
    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    # print(lines)
    count = visibility(lines)
    print(count)

    spot = scenic(lines)
    print(spot)
