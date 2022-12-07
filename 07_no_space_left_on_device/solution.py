def read_file(file_name):
    with open(file_name, "r") as f:
        data = f.read().splitlines()
    return data


EXAMPLE_FILE = "example"
INPUT_FILE = "input"


class Tree:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.directories = {}
        self.files = []
        self.size = 0

    def add_file(self, name, size):
        self.files.append((name, size))

    def add_dir(self, name):
        if name not in self.directories:
            self.directories[name] = Tree(name, self)
        return self.directories[name]

    def get_parent(self):
        return self.parent

    def get_size(self):
        if self.size != 0:
            return self.size
        for _, s in self.files:
            self.size += s
        for directory in self.directories.values():
            self.size += directory.get_size()
        return self.size

    def get_dir_sizes(self):
        sizes = [self.get_size()]
        for directory in self.directories.values():
            sizes.extend(directory.get_dir_sizes())
        return sizes


def prepare_data(file_name):
    file_tree = None
    current_tree = None
    data = read_file(file_name)
    for line in data:
        line = line.split(' ')

        if line[0] == '$':
            if line[1] == 'cd':
                if line[2] == '..':
                    current_tree = current_tree.get_parent()
                else:
                    if file_tree == None:
                        file_tree = Tree(line[2])
                        current_tree = file_tree
                    else:
                        current_tree = current_tree.add_dir(line[2])
            # elif line[1] = 'ls':
        else:
            if line[0] == 'dir':
                current_tree.add_dir(line[1])
            else:
                current_tree.add_file(line[1], int(line[0]))
    return file_tree


tree = prepare_data(EXAMPLE_FILE)
# tree.get_size()
tree.get_dir_sizes()


def solve_part1(file_name):
    result = 0
    tree = prepare_data(file_name)
    dir_sizes = tree.get_dir_sizes()
    for size in dir_sizes:
        if size <= 100000:
            result += size
    return result


print("## Part 1 ##")
print(solve_part1(EXAMPLE_FILE))
print(solve_part1(INPUT_FILE))


def solve_part2(file_name):
    tree = prepare_data(file_name)
    free_space = 70000000 - tree.get_size()
    needed_space = 30000000 - free_space
    dir_sizes = tree.get_dir_sizes()
    candidates = []
    for size in dir_sizes:
        if size >= needed_space:
            candidates.append(size)
    return min(candidates)


print("## Part 2 ##")
print(solve_part2(EXAMPLE_FILE))
print(solve_part2(INPUT_FILE))
