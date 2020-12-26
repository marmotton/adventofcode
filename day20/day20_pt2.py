import numpy as np
from PIL import Image, ImageOps

grid = np.load('solved_grid.npy')
tiles = np.load('tiles.npy').item()  # Extract the dict from the structured array using item()

image = None

# Assemble the tiles into an image
for row in range(len(grid)):
    tiles_row = None
    for col in range(len(grid[row])):
        tile_id = grid[row][col][0]
        tile_image_idx = grid[row][col][1]

        # Remove the borders
        tile_without_borders = tiles[tile_id][tile_image_idx]
        tile_without_borders = np.delete(tile_without_borders, 0, axis=0)
        tile_without_borders = np.delete(tile_without_borders, -1, axis=0)
        tile_without_borders = np.delete(tile_without_borders, 0, axis=1)
        tile_without_borders = np.delete(tile_without_borders, -1, axis=1)

        # Assemble a row of tiles
        if tiles_row is None:
            tiles_row = tile_without_borders
        else:
            tiles_row = np.concatenate((tiles_row, tile_without_borders), axis=1)

    # Assemble the rows of tiles into an image
    if image is None:
        image = tiles_row
    else:
        image = np.concatenate((image, tiles_row), axis=0)

# Generate a mask in the shape of a monster
with open("monster") as f:
    monster = np.array([[True if x == '#' else False for x in line.strip("\n")] for line in f])

# Flip and rotate the whole image until monsters are found
n_monsters = 0
image_without_monsters = None
image_with_highlighted_monsters = None
for flip in [False, True]:
    if flip:
        image = np.flip(image, axis=1)

    for rotation in range(4):
        if image_without_monsters is not None:
            # No need to check other orientations as the correct one (with monsters) has already been found
            break

        if rotation > 0:
            image = np.rot90(image, k=1)

        # Look for monsters
        for y in range(0, len(image) - len(monster)):
            for x in range(0, len(image[0]) - len(monster[0])):
                image_region = image[y:y+len(monster), x:x+len(monster[0])]
                monster_detected = (image_region[monster] == 1).all()

                if monster_detected:
                    if image_without_monsters is None:
                        image_without_monsters = image.copy()
                        image_with_highlighted_monsters = image.copy() * 80.0

                    n_monsters += 1
                    # Remove monster from the image without monsters
                    image_without_monsters[y:y+len(monster), x:x+len(monster[0])][monster] = 0

                    # Highlight the monster
                    image_with_highlighted_monsters[y:y+len(monster), x:x+len(monster[0])][monster] = 255.0

water_roughness = sum(sum(image_without_monsters))

print("Part 2: {} monsters detected. Water roughness is {}".format(n_monsters, water_roughness))

# Save the image as png with some colors
im = Image.fromarray(image_with_highlighted_monsters).convert(mode='L')
im = ImageOps.colorize(im, (8, 91, 120),(232, 91, 19) ,(53, 168, 185))
im.save("sea.png")
