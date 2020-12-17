import copy

def compute_new_seats_state(seats_state):
    new_seats_state = copy.deepcopy(seats_state)

    for i in range(len(seats_state)):
        for j in range(len(seats_state[i])):
            # Count how many adjacent seats are occupied
            n_occupied_adjacent_seats = 0
            for k in range(-1 if i > 0 else 0, 2 if i < len(seats_state)-1 else 1):
                for m in range(-1 if j > 0 else 0, 2 if j < len(seats_state[i])-1 else 1):
                    if seats_state[i+k][j+m] == '#' and (k != 0 or m != 0):
                        n_occupied_adjacent_seats += 1

            # Occupy empty seats that have no neighbors
            if seats_state[i][j] == 'L' and n_occupied_adjacent_seats == 0:
                new_seats_state[i][j] = '#'

            # Free occupied seats that have too many neighbors
            elif seats_state[i][j] == '#' and n_occupied_adjacent_seats >= 4:
                new_seats_state[i][j] = 'L'

    return new_seats_state


def compute_new_seats_state_pt2(seats_state):
    new_seats_state = copy.deepcopy(seats_state)

    for i in range(len(seats_state)):
        for j in range(len(seats_state[i])):
            # Count how many adjacent seats are occupied
            n_occupied_adjacent_seats = 0

            for dir_x in [-1, 0, 1]:
                for dir_y in [-1, 0, 1]:
                    if dir_x != 0 or dir_y != 0:
                        pos = [i, j]
                        while True:
                            pos[0] += dir_x
                            pos[1] += dir_y

                            # Don't search outside the waiting room
                            if pos[0] >= len(seats_state) or pos[1] >= len(seats_state[0]) or pos[0] < 0 or pos[1] < 0:
                                break

                            if seats_state[pos[0]][pos[1]] == '#':
                                n_occupied_adjacent_seats += 1
                                break

                            if seats_state[pos[0]][pos[1]] == 'L':
                                break

            # Occupy empty seats that have no neighbors
            if seats_state[i][j] == 'L' and n_occupied_adjacent_seats == 0:
                new_seats_state[i][j] = '#'

            # Free occupied seats that have too many neighbors
            elif seats_state[i][j] == '#' and n_occupied_adjacent_seats >= 5:
                new_seats_state[i][j] = 'L'

    return new_seats_state


with open("input") as f:
    layout = [[seat for seat in line.strip()] for line in f]

# Part 1: find out in what state it stabilizes
seats_state = layout
while True:
    new_seats_state = compute_new_seats_state(seats_state)

    if new_seats_state == seats_state:
        break

    seats_state = new_seats_state

# Count how many seats are occupied
n_occupied_seats = sum([line.count('#') for line in seats_state])

print("Part 1: {} seats are occupied".format(n_occupied_seats))


# Part 2: find out in what state it stabilizes with the new rules
seats_state = layout
while True:
    new_seats_state = compute_new_seats_state_pt2(seats_state)

    if new_seats_state == seats_state:
        break

    seats_state = new_seats_state

# Count how many seats are occupied
n_occupied_seats = sum([line.count('#') for line in seats_state])

print("Part 2: {} seats are occupied".format(n_occupied_seats))
