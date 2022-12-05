with open('input') as f:
    route = [(line[0], int(line[1:])) for line in f]

pos = {'easting': 0, 'northing': 0, 'bearing': 90}

for instruction in route:
    if instruction[0] == 'N':
        pos['northing'] += instruction[1]

    elif instruction[0] == 'S':
        pos['northing'] -= instruction[1]

    elif instruction[0] == 'E':
        pos['easting'] += instruction[1]

    elif instruction[0] == 'W':
        pos['easting'] -= instruction[1]

    elif instruction[0] == 'F':
        if pos['bearing'] == 90:
            pos['easting'] += instruction[1]

        elif pos['bearing'] == 270:
            pos['easting'] -= instruction[1]

        elif pos['bearing'] == 0:
            pos['northing'] += instruction[1]

        elif pos['bearing'] == 180:
            pos['northing'] -= instruction[1]

    elif instruction[0] == 'R':
        pos['bearing'] += instruction[1]

    elif instruction[0] == 'L':
        pos['bearing'] -= instruction[1]

    if pos['bearing'] >=360:
        pos['bearing'] -= 360

    elif pos['bearing'] < 0:
        pos['bearing'] += 360

manhattan_distance = abs(pos['easting']) + abs(pos['northing'])
print("Part1: Manhattan distance is {}".format(manhattan_distance))


# Part 2
def rotate(pt, angle):
    rotated = {  0: pt,
                90: [pt[1], -pt[0]],
               180: [-pt[0], -pt[1]],
               270: [-pt[1], pt[0]],
    }
               
    return rotated[angle]

pos = {'easting': 0, 'northing': 0}
waypoint = {'easting': 10, 'northing': 1}

for instruction in route:
    if instruction[0] == 'N':
        waypoint['northing'] += instruction[1]

    elif instruction[0] == 'S':
        waypoint['northing'] -= instruction[1]

    elif instruction[0] == 'E':
        waypoint['easting'] += instruction[1]

    elif instruction[0] == 'W':
        waypoint['easting'] -= instruction[1]

    elif instruction[0] == 'R':
        waypoint['easting'], waypoint['northing'] = rotate((waypoint['easting'], waypoint['northing']), instruction[1])

    elif instruction[0] == 'L':
        angle = 360 - instruction[1]
        waypoint['easting'], waypoint['northing'] = rotate((waypoint['easting'], waypoint['northing']), angle)

    elif instruction[0] == 'F':
        pos['easting'] += waypoint['easting'] * instruction[1]
        pos['northing'] += waypoint['northing'] * instruction[1]

manhattan_distance = abs(pos['easting']) + abs(pos['northing'])
print("Part2: Manhattan distance is {}".format(manhattan_distance))
