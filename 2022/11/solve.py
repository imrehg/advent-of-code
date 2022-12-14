import sys
import math
import operator
import functools


@functools.cache
def testing_num(number, divisor):
    return number % divisor == 0


class Monkey:

    def __init__(self, name: int, starting_items: list[int], operation, test_num, true_target, false_target):
        self.name = name
        self.starting_items = starting_items
        self.items = self.starting_items.copy()
        self.operation = operation
        self.test_num = test_num
        self.true_target = true_target
        self.false_target = false_target
        self.total_inspections = 0

    def reset(self):
        self.items = self.starting_items.copy()
        self.total_inspections = 0

    def __repr__(self) -> str:
        return f"Monkey {self.name}, holding: {[item for item in self.items]}, operate as {self.operation}, div by {self.test_num}, passing to {self.true_target}|{self.false_target}"

    def do_round(self, monkeys, divisor, modulo = None):
        while self.items:
            self.total_inspections += 1
            old = self.items.pop(0)
            new = eval(self.operation)
            # print(old, self.operation, new)
            new = new // divisor
            if modulo is not None:
                new = new % modulo
            # print(new)
            target = self.true_target if testing_num(new, self.test_num) else self.false_target
            # print(target)
            monkeys[target].items.append(new)

if __name__ == "__main__":
    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    monkyes: dict[int, Monkey] = {}
    for i in range(0, len(lines), 7):
        m = lines[i:i+6]
        name = int(m[0].split()[1].rstrip(":"))
        items = [int(item.rstrip(",")) for item in m[1].split(":")[1].split()]
        operation = m[2].split("=")[1].strip()
        test_num = int(m[3].split()[-1])
        true_target = int(m[4].split()[-1])
        false_target = int(m[5].split()[-1])
        x = Monkey(name, items, operation, test_num, true_target, false_target)
        monkyes[name] = x
        print(x)

    monkey_order = sorted(monkyes.keys())

    n_rounds = 20
    for i_round in range(n_rounds):
        for m in monkey_order:
            monkyes[m].do_round(monkyes, divisor = 3, modulo=None)
            # print(monkyes)
            # print("\n\n")
            # break

    x = math.prod(sorted([monkyes[m].total_inspections for m in monkey_order], reverse=True)[:2])
    print(x)


    # again
    for m in monkey_order:
        monkyes[m].reset()
    modulo = math.prod([monkyes[m].test_num for m in monkey_order])
    # print(modulo)

    n_rounds = 10_000
    for i_round in range(n_rounds):
        # if i_round % 1000 == 0 or i_round == 20 or i_round == 1:
        #     print([monkyes[m].total_inspections for m in monkey_order])
        for m in monkey_order:
            monkyes[m].do_round(monkyes, divisor = 1, modulo=modulo)
            # print([monkyes[m].total_inspections for m in monkey_order])
            # break
            # print(monkyes)
            # print("\n\n")
            # break
    # print([monkyes[m].total_inspections for m in monkey_order])
    x = math.prod(sorted([monkyes[m].total_inspections for m in monkey_order], reverse=True)[:2])
    print(x)