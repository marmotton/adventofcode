with open("input") as f:
    topo_str = f.readlines()

topo = [[char == '#' for char in line.strip()] for line in topo_str]

x_length = len(topo[0])

n_trees_multiplied = 1
n_trees_slope_1_2 = 0

for x_increment in [1, 3, 5, 7]:
    n_trees = 0
    x_pos = 0
    for line in topo:
        # Check if there is a tree
        if line[x_pos % x_length]:
            n_trees = n_trees + 1
                
        x_pos = x_pos + x_increment

    if x_increment == 3:
        print("Part 1: {} trees".format(n_trees))
    
    n_trees_multiplied = n_trees_multiplied * n_trees

# Slope 1 right 2 down
x_pos = 0
for line in topo[::2]:
    # Check if there is a tree
    if line[x_pos % x_length]:
        n_trees_slope_1_2 = n_trees_slope_1_2 + 1
            
    x_pos = x_pos + 1

n_trees_multiplied = n_trees_multiplied * n_trees_slope_1_2

print("Part 2: {}".format(n_trees_multiplied))
