puzzle_input = "364297581"


def play(cups, rounds):
    for __ in  range(rounds):
        current_cup = cups[0]

        # Put the current cup at the end
        cups.append(current_cup)
        cups = cups[1:]

        # Remove 3 cups
        removed_cups = cups[:3]
        cups = cups[3:]

        # Find the destination cup
        destination_cup = current_cup
        while True:
            if destination_cup > 1:
                destination_cup -= 1
            else:
                destination_cup = max(cups)

            if destination_cup in cups:
                break

        # Place the cups after the destination cup
        destination_idx = cups.index(destination_cup) + 1
        cups[destination_idx:destination_idx] = removed_cups

    return cups


# Part 1
cups = [int(c) for c in puzzle_input]

cups = play(cups, 100)

# The result is the order of the cups after cup 1
cup_1_idx = cups.index(1)
cups_after_1 = cups[cup_1_idx+1:]
cups_after_1.extend(cups[:cup_1_idx])

result = ""
for cup in cups_after_1:
    result += str(cup)

print("Part 1: order is {}".format(result))


# Part 2
def play_pt2(cups, rounds):
    # next_cup[cup number] = next cup number
    next_cup = [None] * (len(cups) + 1)  # +1 as index 0 is not used

    # Assign next_cup using the order of cups
    for i in range(1, len(next_cup)):
        if i < len(cups):
            next_cup[cups[i-1]] = cups[i]
        else:
            next_cup[cups[i-1]] = cups[0]

    current_cup = cups[0]
    for i in range(rounds):
        # Remove 3 cups
        removed_cups = [next_cup[current_cup]]
        for j in range(1,3):
            removed_cups.append(next_cup[removed_cups[j-1]])
        
        # Close the gap left by the 3 removed cups
        next_cup[current_cup] = next_cup[removed_cups[2]]

        # Find the destination cup
        destination_cup = current_cup
        while True:
            if destination_cup > 1:
                destination_cup -= 1
            else:
                destination_cup = max(cups)

            if destination_cup not in removed_cups:
                break

        # Insert the 3 removed cups after the destination cup
        next_cup[removed_cups[2]] = next_cup[destination_cup]
        next_cup[destination_cup] = removed_cups[0]

        # Update the current cup
        current_cup = next_cup[current_cup]

    # Return the list of cups in the correct order, starting at cup 1
    cups[0] = 1
    for i in range(len(cups) - 1):
        cups[i+1] = next_cup[cups[i]]
    return cups

# Add more cups up to 1 million
cups = [int(c) for c in puzzle_input]
cups.extend(list(range(len(cups)+1, 1000001)))

# Play 10 million moves
cups = play_pt2(cups, 10000000)

print("Part 2: {} * {} = {}".format(cups[1], cups[2], cups[1] * cups[2]))
