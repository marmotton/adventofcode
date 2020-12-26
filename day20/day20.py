import math
import numpy as np

tiles = {}

with open("input_example") as f:
    all_tiles_str = f.read().strip().split("\n\n")

    for tile_str in all_tiles_str:
        tile_id = None
        tile_image = []
        for line in tile_str.split("\n"):
            if line.startswith("Tile"):
                tile_id = int(line[5:].strip(":\n"))
            else:
                pixels = [1 if x == '#' else 0 for x in line.strip()]
                tile_image.append(pixels)

        # Generate all possible orientations (4 rotations and flip/no-flip = 8 possibilities)
        tile = np.array(tile_image)
        all_orientations = []
        for flip in [False, True]:
            if flip:
                tile = np.flip(tile, axis=1)

            for rotation in range(4):
                if rotation > 0:
                    tile = np.rot90(tile, k=1)
                
                all_orientations.append(tile)

        tiles[tile_id] = all_orientations

# The tiles will be arranged on a grid_size * grid_size grid
grid_size = int(math.sqrt(len(tiles)))
grid = np.zeros((grid_size, grid_size, 2), dtype=int)  # grid[row][col] = [tile_id, tile_image_idx]


def tile_fits(tile_id, tile_image_idx, position):
    # Check if the tile is already used in the image using its ID
    already_used_tiles = set(grid[::,:,0].flatten())
    if tile_id in already_used_tiles:
        return False

    # Check if the tile borders line up with adjacent tiles that are already placed
    for (dx, dy) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        tile_pos_to_check = (position[0] + dy, position[1] + dx)

        # Check the tile if it is on the grid (= not outside)
        if 0 <= tile_pos_to_check[0] < grid_size and 0 <= tile_pos_to_check[1] < grid_size:
            tile_id_to_check = grid[tile_pos_to_check][0]
            tile_image_idx_to_check = grid[tile_pos_to_check][1]

            # Only do the check if there is a tile in this location (non-empty grid cells)
            if tile_id_to_check > 0:
                if dy == 1:  # Check against tile below
                    line_of_tile = tiles[tile_id][tile_image_idx][-1]  # Bottom row
                    line_of_adjacent_tile = tiles[tile_id_to_check][tile_image_idx_to_check][0]  # Top row
                elif dy == -1:  # Check against tile above
                    line_of_tile = tiles[tile_id][tile_image_idx][0]  # Top row
                    line_of_adjacent_tile = tiles[tile_id_to_check][tile_image_idx_to_check][-1]  # Bottom row
                elif dx == 1:  # Check against tile on the right
                    line_of_tile = tiles[tile_id][tile_image_idx][:,-1]  # Right col
                    line_of_adjacent_tile = tiles[tile_id_to_check][tile_image_idx_to_check][:,0]  # Left col
                elif dx == -1:  # Check against tile on the left
                    line_of_tile = tiles[tile_id][tile_image_idx][:,0]  # Left col
                    line_of_adjacent_tile = tiles[tile_id_to_check][tile_image_idx_to_check][:,-1]  # Right col

                # The 2 neighbouring lines are selected, we can abort now if they're different, otherwise we continue checking other tiles
                if (line_of_tile != line_of_adjacent_tile).any():
                    return False

    # We encountered no non-matching tile, i.e. the tile can be placed in the requested position
    return True


solved_grid = None
solving_done = False
def solve():  # Inspired by https://www.youtube.com/watch?v=G_UYXzGuqvM
    global grid, solved_grid, solving_done

    # Solve unless a solution has been found
    if solving_done == False:
        # Go through each cell in the grid
        for row in range(grid_size):
            for col in range(grid_size):
                # Try to place a tile if the cell is empty (i.e. if the tile_id of the cell is 0)
                if grid[row][col][0] == 0:
                    for tile_id, all_orientations in tiles.items():
                        for tile_image_idx in range(len(all_orientations)):
                            if tile_fits(tile_id=tile_id, tile_image_idx=tile_image_idx, position=(row, col)):
                                grid[row][col][0] = tile_id
                                grid[row][col][1] = tile_image_idx
                                # The tile has been placed successfully, we can solve for the next tiles
                                # This call to solve() will start from the next tile as we placed a new tile into the grid
                                solve()
                                # We end up here if solve() returned, i.e. if the rest of the grid couldn't be filled successfuly
                                # This means that we put the wrong tile into the grid, remove it
                                grid[row][col][0] = 0
                                grid[row][col][1] = 0

                    # We tried every possibility but failed, let's return to the caller so he can choose another previous tile
                    return

        # We end up here when solve() is called just after the last cell has been filled successfully
        # i.e. when all the cells are filled --> a solution has been found
        solved_grid = grid.copy()
        solving_done = True  # Avoid looking for other solutions (all the rotations and flipping of the whole picture)


solve()

# Save results for part 2
np.save('solved_grid.npy', solved_grid)
np.save('tiles.npy', tiles)


corners = [solved_grid[0, 0][0], solved_grid[0, grid_size - 1][0], solved_grid[grid_size - 1, grid_size - 1][0], solved_grid[grid_size - 1, 0][0]]
result = np.product(corners)
print("Part 1: {} * {} * {} * {} = {}".format(corners[0], corners[1], corners[2], corners[3], result))
