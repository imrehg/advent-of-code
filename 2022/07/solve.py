import sys

class DirNode:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

class FileNode:
    def __init__(self, filename, size=0):
        self.name = filename
        self.size = size
        self.parent = None


silver_total = 0
dir_sizes = []

def process(lines):

    current_node = None
    root_node = None

    for line in lines:
        # print(f"{current_node.name if current_node is not None else ''}")
        if line.startswith("$ cd "):
            new_folder = line[5:]
            # print("-->", new_folder)
            if new_folder not in {"..", "/"}:
                new_node = DirNode(new_folder)
                if current_node is not None:
                    current_node.add_child(new_node)
                else:
                    root_node = new_node
                current_node = new_node
            elif new_folder == "..":
                current_node = current_node.parent
            elif new_folder == "/":
                if root_node is None:
                    root_node = DirNode(new_folder)
                current_node = root_node
            # print(current_node.name)
        elif not line.startswith("$"):
            part1, part2 = line.split()
            if part1 != "dir":
                new_file = FileNode(part2, int(part1))
                current_node.add_child(new_file)

    # root_node.print_tree()

    def get_all_filesize(dir: DirNode):
        global silver_total
        global dir_sizes
        total = 0
        for child in dir.children:
            if type(child) is DirNode:
                total += get_all_filesize(child)
            else:
                total += child.size
        # print(dir.name, total)
        if total <= 100_000:
            silver_total += total
        dir_sizes += [total]
        return total

    total = get_all_filesize(root_node)
    print(silver_total)

    max_space = 70_000_000
    free_space = max_space - total
    space_needed = 30_000_000 - free_space
    global dir_sizes
    dir_sizes = sorted(dir_sizes)
    for value in dir_sizes:
        if value >= space_needed:
            print(value)
            break

if __name__ == "__main__":
    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    structure = process(lines)