import sys


class BingoBoard:
    def __init__(self, layout):
        self.layout = layout
        self.values = {}
        for row in layout:
            for value in row:
                self.values[value] = False

    def mark(self, number):
        if number in self.values:
            self.values[number] = True
        return self.check_bingo()

    def check_bingo(self):
        bingo = False
        for row in self.layout:
            row_check = all([self.values[value] for value in row])
            if row_check:
                bingo = True
                break

        for col_index in range(len(self.layout[0])):
            col_check = all(
                [
                    self.values[self.layout[row_index][col_index]]
                    for row_index in range(len(self.layout[0]))
                ]
            )
            if col_check:
                bingo = True
                break
        return bingo

    def get_unmarked(self):
        unmarked = [number for number in self.values.keys() if not self.values[number]]
        return unmarked

    def reset_board(self):
        for value in self.values:
            self.values[value] = False


if __name__ == "__main__":
    input_file = sys.argv[1]

    boards = []
    with open(input_file, "r") as f:
        numbers = [int(n) for n in f.readline().strip().split(",")]
        while True:
            header_line = f.readline()
            if len(header_line) == 0:
                break
            board = []
            for _ in range(5):
                row = f.readline().strip().split()
                board += [[int(n) for n in row]]
            boards += [BingoBoard(board)]

    for number in numbers:
        finished = False
        for board in boards:
            got_bingo = board.mark(number)
            if got_bingo:
                print(f"Bingo!: {number}")
                finished = True
                unmarked = board.get_unmarked()
                result = sum(unmarked) * number
                print(result)
                break
        if finished:
            break

    for board in boards:
        board.reset_board()

    print(">>> Part2")
    for number in numbers:
        finished = False
        boards_continue = []
        last_board = None
        for board in boards:
            got_bingo = board.mark(number)
            if not got_bingo:
                boards_continue += [board]
            else:
                last_board = board

        if len(boards_continue) == 0:
            print(sum(last_board.get_unmarked()) * number)
            finished = True
            break
        else:
            boards = boards_continue
        if finished:
            break
