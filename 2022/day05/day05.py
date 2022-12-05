import re

with open('input') as input:
    # How many stacks ? (\n is also included in length)
    n_stacks = len(input.readline()) // 4

    initial_stacks = [ [] for _ in range(n_stacks) ]  # [[]] * n_stacks creates references to the same object

    # Read the initial state of the stacks
    input.seek(0)
    for line in input:

        if line[1] == '1':
            break

        for i in range(0, n_stacks):
            col = 4 * i + 1
            if line[col] != ' ':
                initial_stacks[i].insert(0, line[col])

    stacks_pt1 = [ x.copy() for x in initial_stacks]
    stacks_pt2 = [ x.copy() for x in initial_stacks]

    # Move the crates
    for line in input:
        m = re.fullmatch(r'^move (\d+) from (\d+) to (\d+)$', line.strip())

        if m is not None:
            qty = int(m[1])
            frm = int(m[2]) - 1
            to = int(m[3]) - 1
            
            for i in range(qty):
                stacks_pt1[to].append( stacks_pt1[frm].pop() )
                stacks_pt2[to].insert( len(stacks_pt2[to]) - i, stacks_pt2[frm].pop() )

    # Crates on the top
    res = ""
    for stack in stacks_pt1:
        res += stack[-1]
    print("Part 1: {}".format(res))

    res = ""
    for stack in stacks_pt2:
        res += stack[-1]
    print("Part 2: {}".format(res))
    