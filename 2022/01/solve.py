import sys

if __name__ == "__main__":
    input_file = sys.argv[1]

    with open(input_file) as f:
        input = [line.strip() for line in f.readlines()]

    # print(input)
    currentval = 0
    maxval = 0
    for val in input:
        if len(val) > 0:
            currentval += int(val)
        else:
            if currentval > maxval:
                maxval = currentval
            currentval = 0
    if currentval > maxval:
        maxval = currentval
    currentval = 0

    print(maxval)


    sums = []
    currentval = 0
    for val in input:
        if len(val) > 0:
            currentval += int(val)
        else:
            sums.append(currentval)
            currentval = 0
    if currentval > 0:
        sums.append(currentval)

    # print(sums)
    x = sum(sorted(sums, reverse=True)[0:3])
    print(x)
