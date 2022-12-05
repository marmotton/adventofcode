with open('input') as input:
    sections_pt2 = []

    n_containing_sets = 0

    for line in input:
        ranges = line.strip().split(',')  # e.g. ["34-75", "12-70"]

        # Convert ranges "xx-yy" into sets containing every number in the range
        sections = []
        for i in range(2):
            range_start_stop = [int(x) for x in ranges[i].split('-')]

            sections.append( set(range(range_start_stop[0], range_start_stop[1] + 1) ) )

        sections_pt2.append(sections)

        # Find out if a range is contained in the other
        if sections[0].issubset( sections[1] ) or sections[1].issubset( sections[0] ):
            n_containing_sets += 1

    print("Part 1: {}".format(n_containing_sets))

    # Part 2
    n_overlapping_sets = 0
    for sections in sections_pt2:
        if not sections[0].isdisjoint(sections[1]):
            n_overlapping_sets += 1
    
    print("Part 2: {}".format(n_overlapping_sets))
