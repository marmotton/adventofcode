import re

class FSelement:
    def __init__(self, parent, name, size=0, is_dir=True):
        self.parent = parent
        self.children = set()
        self.name = name
        self.size = int(size)
        self.is_dir = is_dir

        if self.parent is not None:
            self.parent.add_size(size)

    def add_file(self, name, size):
        new_file = FSelement(self, name, size, False)
        self.children.add( new_file )

    def add_dir(self, name):
        new_dir = FSelement(self, name)
        self.children.add(new_dir)

    def add_size(self, size):
        self.size += int(size)
        if self.parent is not None:
            self.parent.add_size(size)

    def cd(self, target):
        if target == '..':
            return self.parent
        else:
            for child in self.children:
                if child.name == target:
                    return child
            return None


def part1(fs):
    sum = 0
    for child in fs.children:
        if child.is_dir:
            if child.size <= 100000:
                sum += child.size
            sum += part1(child)
    return sum


fs = FSelement(None, '/')
with open('input') as input:
    current_dir = fs
    current_cmd = ''

    for line in input:
        l = line.strip()

        # The Python 3.10 match..case could be used here, e.g. using ["$", "cd", name]
        if l.startswith('$'):
            current_cmd = l[2:]
            if current_cmd == 'ls':
                continue

        if current_cmd.startswith('cd'):
            target = current_cmd[3:]

            if target == '/':
                current_dir = fs
            else:
                current_dir = current_dir.cd( target )

        if current_cmd.startswith('ls'):
            if l.startswith('dir'):
                dir_name = l[4:]
                current_dir.add_dir(dir_name)

            else:
                m = re.fullmatch(r'^(\d+) (.+)$', l)
                size = int(m[1])
                file_name = m[2]
                current_dir.add_file(file_name, size)

print( "Part 1: {}".format( part1(fs) ) )

# Part 2
total_space = 70000000
needed_space = 30000000
delete_at_least = needed_space - (total_space - fs.size)

candidates_sizes = []

def part2(fs):
    if fs.size >= delete_at_least:
        candidates_sizes.append(fs.size)

    for child in fs.children:
        if child.is_dir:
            part2(child)
    return

part2(fs)
candidates_sizes.sort()
print("Part 2: {}".format( candidates_sizes[0] ) )
