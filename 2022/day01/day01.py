with open('input', newline='\n') as input:
    sums = [0]
    for line in input:
        if line == "\n":
            sums.append(0)
        else:
            sums[-1] += int(line.strip())

    print("Part 1: {}".format(max(sums)))

    # Part 2
    sums.sort()
    print("Part 2: {}".format( sum( sums[-3:] ) ) )
