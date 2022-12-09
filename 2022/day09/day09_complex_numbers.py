# Learning from this solution: https://www.reddit.com/r/adventofcode/comments/zgnice/comment/iziqhsx/

with open('input') as input:
    # Create a lookup table (dict) listing moves according to distance
    # 2D position is represented by complex numbers (x+yj)
    # := is used to assign a value to a variable within an expression (https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions PEP 572)
    # if dx or dy < 0, it will read moves[] from the end
    distances = [-2, -1, 0, 1, 2]
    moves = [0, -1, -1, 1, 1]
    follow = { (a := dx + dy*1j): moves[dx] + moves[dy]*1j if abs(a)>=2 else 0 for dx in distances for dy in distances }

    visited_pt1 = set()
    visited_pt2 = set()
    rope = [0] * 10

    for line in input:
        direction = {'R':1, 'L':-1, 'U':1j, 'D':-1j}[line[0]]
        steps = int(line[2:])

        for _ in range(steps):
            # Move head
            rope[0] += direction
            
            # Move tail
            for k in range(1, len(rope)):
                dist = rope[k] - rope[k - 1]
                rope[k] += follow[dist]

            visited_pt1.add( rope[1] )
            # Another way of adding to a set
            visited_pt2 |= {rope[-1]}

    print("Part 1: {}".format(len(visited_pt1)))
    print("Part 2: {}".format(len(visited_pt2)))
