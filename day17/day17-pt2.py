import copy

with open("input") as f:
    initial_slice = [[True if c == '#' else False for c in line.strip()] for line in f]

total_cycles = 6

# Initialize all cells to False. The grid size depends on the number of cycles.
grid = [[[[False for x in range(len(initial_slice[0]) + 2*total_cycles + 2)] for y in range(len(initial_slice) + 2*total_cycles + 2)] for z in range(1 + 2*total_cycles + 2)] for w in range(1 + 2*total_cycles + 2)]

# Set the initial values
for i in range(len(initial_slice)):
    for j in range(len(initial_slice[0])):
        grid[total_cycles + 1][total_cycles + 1][i + total_cycles + 1][j + total_cycles + 1] = initial_slice[i][j]

# Play the cycles
offsets = []
for i in range(-1, 2):
    for j in range(-1, 2):
        for k in range(-1, 2):
            for l in range(-1, 2):
                if i != 0 or j != 0 or k != 0 or l != 0:
                    offsets.append([i, j, k, l])

total_active_cells = 0
for cycle in range(total_cycles):
    new_grid = copy.deepcopy(grid)
    total_active_cells = 0
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            for k in range(1, len(grid[i][j]) - 1):
                for l in range(1, len(grid[i][j][k]) - 1):
                    # Count how many neighbors are active
                    active_neighbors = 0
                    for offset in offsets:
                        if grid[i + offset[0]][j + offset[1]][k + offset[2]][l + offset[3]]:
                            active_neighbors += 1

                    # Set the new values according to the rules
                    if grid[i][j][k][l]:
                        if active_neighbors < 2 or active_neighbors > 3:
                            new_grid[i][j][k][l] = False
                    else:
                        if active_neighbors == 3:
                            new_grid[i][j][k][l] = True

                    if new_grid[i][j][k][l]:
                        total_active_cells += 1
    grid = new_grid

print("Part 2: {} active cubes".format(total_active_cells))
