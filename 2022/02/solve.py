import sys

if __name__ == "__main__":
    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    
    
    total = 0
    sum = 0
    for line in lines:
        sum = 0
        c = line.split(" ")
        win = (c[0] == 'A' and c[1] == 'Y') or (c[0] == 'B' and c[1] == 'Z') or (c[0] == 'C' and c[1] == 'X')
        draw = (c[0] == 'A' and c[1] == 'X') or (c[0] == 'B' and c[1] == 'Y') or (c[0] == 'C' and c[1] == 'Z')
        lost = (not win) and (not draw)
        if c[1] == 'X':
            sum += 1
        elif c[1] == 'Y':
            sum += 2
        else :
            sum += 3

        if win:
            sum += 6
        elif draw:
            sum += 3
        total += sum
        print(total, sum)

    print(total)

    winmap = {"A": "Y", "B": "Z", "C": "X"}
    drawmap = {"A": "X", "B": "Y", "C": "Z"}
    losemap = {"A": "Z", "B": "X", "C": "Y"}
    scoremap = {"X": 1, "Y": 2, "Z": 3}

    total = 0
    sum = 0
    for line in lines:
        sum = 0
        c = line.split(" ")
        if c[1] == 'X':
            sum += scoremap[losemap[c[0]]]
        elif c[1] == 'Y':
            sum += 3
            sum += scoremap[drawmap[c[0]]]
        else:
            sum += 6
            sum += scoremap[winmap[c[0]]]
        total += sum    

    print(total)