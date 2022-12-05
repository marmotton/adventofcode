def priority(c):
    res = ord(c) - 96  # a-z --> 1-26

    if res < 1:
        res += 32 + 26  # A-Z --> 27-52
    return res


with open('input') as input:
    rucksack_content = []

    for line in input:
        contents = line.strip()
        n_items = len(contents)
        rucksack_content.append( (contents[:n_items // 2], contents[n_items // 2:], set(contents)) )  # set(contents) is for part 2

    sum_of_priorities = 0
    for content in rucksack_content:
        # Find which item (letter) is in both pockets
        for item in content[0]:
            if item in content[1]:
                sum_of_priorities += priority(item)
                break

    print("Part 1: {}".format(sum_of_priorities))

    # Part 2
    sum_of_priorities = 0
    for i in range(0, len(rucksack_content), 3):
        badge = set.intersection(rucksack_content[i][2], rucksack_content[i+1][2], rucksack_content[i+2][2])
        sum_of_priorities += priority( list(badge)[0] )

    print("Part 2: {}".format(sum_of_priorities))
