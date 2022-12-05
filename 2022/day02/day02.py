with open('input') as input:
    rounds = [line.strip().split() for line in input]

    score = 0

    for r in rounds:
        # Shape component of the score
        shape_value = {'X': 1, 'Y': 2, 'Z': 3}
        score += shape_value[ r[1] ]

        # A/X: Rock
        # B/Y: Paper
        # C/Z: Scissors
        wins = {'X': 'C', 'Y': 'A', 'Z': 'B'}
        draw = {'X': 'A', 'Y': 'B', 'Z': 'C'}

        if wins[ r[1] ] == r[0]:
            score += 6
        elif draw[ r[1] ] == r[0]:
            score += 3

    print("Part 1: {}".format(score))

    # Part 2
    score = 0
    for r in rounds:
        # A: Rock
        # B: Paper
        # C: Scissors
        # X: loose
        # Y: draw
        # Z: win

        # key is what the oppenent plays, value is what I have to play
        wins = {'A': 'B', 'B': 'C', 'C': 'A'}
        looses = {v: k for k, v in wins.items()}

        shape_value = {'A': 1, 'B': 2, 'C': 3}

        # Loose
        if r[1] == 'X':
            score += shape_value[ looses[ r[0] ] ]
        # Draw
        elif r[1] == 'Y':
            score += shape_value[ r[0] ] + 3
        # Win
        else:
            score += shape_value[ wins[ r[0] ] ] + 6

    print("Part 2: {}".format(score))
