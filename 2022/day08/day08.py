import numpy as np

forest = np.genfromtxt('input', dtype=np.short, delimiter=1)

def detect_visible_trees(line):
    visible_trees = [0] * len(line)

    tallest_tree = -1

    for idx, size in enumerate(line):
        if size > tallest_tree:
            visible_trees[idx] = 1
            tallest_tree = size

    return visible_trees

visible_trees = forest.copy() * 0

for idx, row in enumerate(forest):
    # Left to right
    visible_trees[idx] |= detect_visible_trees(row)
    
    # Right to left
    visible_trees[idx] |= detect_visible_trees(row[::-1])[::-1]

for idx, col in enumerate(forest.T):
    # Top to bottom
    visible_trees[:,idx] |= detect_visible_trees(col)

    # Bottom to top
    visible_trees[:,idx] |= detect_visible_trees(col[::-1])[::-1]

print("Part 1: {}".format(np.sum(visible_trees)))

# Part 2
def line_scenic_score(line):
    scenic_score = 0
    my_tree_size = line[0]

    for size in line[1:]:
        scenic_score += 1
        if size >= my_tree_size:
            break

    return scenic_score

    
max_scenic_score = 0

for rownum in range( 1, forest.shape[0] - 1 ):
    for colnum in range( 1, forest.shape[1] - 1 ):
        scenic_score = 1
        # Looking to the right
        scenic_score *= line_scenic_score( forest[rownum, colnum:] )

        # Looking to the left
        scenic_score *= line_scenic_score( forest[rownum, :colnum+1][::-1] )

        # Looking down
        scenic_score *= line_scenic_score( forest[rownum:, colnum] )

        # Looking up
        scenic_score *= line_scenic_score( forest[:rownum+1, colnum][::-1] )

        max_scenic_score = max(max_scenic_score, scenic_score)

print("Part 2: {}".format(max_scenic_score))
