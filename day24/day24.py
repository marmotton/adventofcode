moves = []

with open('input') as f:
    modifier_char = ""  # Used for 2-chars moves (ne, sw...)
    for line in f:
        tile_path = []
        for c in line.strip():
            if c in ['n', 's']:
                modifier_char = c
            else:
                tile_path.append(modifier_char + c)
                modifier_char = ""
        moves.append(tile_path)

# Hexagonal grid, 2 coordinates (x,y). X axis is the East-West direction, Y axis is the Southeast-Northwest direction.
# East: X+
# West: X-
# Southeast: Y+
# Northwest: Y-
# Northeast: X+, Y-
# Southwest: X-, Y+

# Map direction into a X/Y displacement
move_to_xy = {
     'e' : (1, 0),
     'w' : (-1, 0),
    'se' : (0, 1),
    'nw' : (0, -1),
    'ne' : (1, -1),
    'sw' : (-1, 1)
}

black_tiles = set()

for tile_path in moves:
    # Start on the center tile at (0,0)
    x = 0
    y = 0

    # Follow the path
    for direction in tile_path:
        x += move_to_xy[direction][0]
        y += move_to_xy[direction][1]
    
    # Flip the tile
    tile = (x, y)
    if tile not in black_tiles:
        black_tiles.add(tile)
    else:
        black_tiles.remove(tile)

print("Part 1: {} tiles are black".format(len(black_tiles)))

# Part 2
def adjacent_black_tiles(tile):
    n_adjacent_black_tiles = 0
    # Count the number of black tiles at each of the 6 positions around the given tile
    for move in move_to_xy.values():
        if (tile[0] + move[0], tile[1] + move[1]) in black_tiles:
            n_adjacent_black_tiles += 1

    return n_adjacent_black_tiles

days = 100
for _ in range(days):
    new_black_tiles = set()

    for tile in black_tiles:
        # Black tiles with 1 or 2 adjacent black tiles stay black. (opposite of =0 or >2)
        if 1 <= adjacent_black_tiles(tile) <= 2:
            new_black_tiles.add(tile)

        # Check the 6 adjacent tiles if they are white. White tiles with 2 adjacent black tiles are flipped to black.
        for move in move_to_xy.values():
            maybe_white_tile = (tile[0] + move[0], tile[1] + move[1])

            if maybe_white_tile not in black_tiles:
                # The tile is white
                if adjacent_black_tiles(maybe_white_tile) == 2:
                    new_black_tiles.add(maybe_white_tile)

    black_tiles = new_black_tiles

print("Part 2: {} tiles are black after {} days".format(len(black_tiles), days))
