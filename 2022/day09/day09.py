def add_pos(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

def dist(t1, t2):
    return (t2[0] - t1[0], t2[1] - t1[1])

with open('input') as input:
    hpos = (0, 0)
    tpos = (0, 0)
    visited_tpos = {(0, 0)}

    move = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

    # For part 2
    rope = [(0, 0)] * 10
    visited_tpos_pt2 = {(0, 0)}

    for line in input:
        direction, steps = line.split()
        steps = int(steps)
        
        for i in range(steps):
            # Move head
            hpos = add_pos(hpos, move[direction])
            
            # Move tail
            htdist = dist(tpos, hpos)

            # Horizontal move
            if htdist[1] == 0 and abs(htdist[0]) == 2:
                tpos = add_pos(tpos, (htdist[0] // 2, 0) )
            # Vertical move
            elif htdist[0] == 0 and abs(htdist[1]) == 2:
                tpos = add_pos(tpos, (0, htdist[1] // 2))
            # Diagonal move
            elif abs(htdist[0]) == 2 or abs(htdist[1]) ==  2:
                hmove = htdist[0] // abs(htdist[0])
                vmove = htdist[1] // abs(htdist[1])
                tpos = add_pos(tpos, (hmove, vmove))

            visited_tpos.add(tpos)

            # Part 2 (would also work for pt1 with a rope length of 2)
            rope[0] = hpos

            for knot_no in range(1, len(rope)):
                knot_dist = dist(rope[knot_no], rope[knot_no - 1])

                # Horizontal move
                if knot_dist[1] == 0 and abs(knot_dist[0]) == 2:
                    rope[knot_no] = add_pos(rope[knot_no], (knot_dist[0] // 2, 0) )
                # Vertical move
                elif knot_dist[0] == 0 and abs(knot_dist[1]) == 2:
                    rope[knot_no] = add_pos(rope[knot_no], (0, knot_dist[1] // 2))
                # Diagonal move
                elif abs(knot_dist[0]) == 2 or abs(knot_dist[1]) ==  2:
                    hmove = knot_dist[0] // abs(knot_dist[0])
                    vmove = knot_dist[1] // abs(knot_dist[1])
                    rope[knot_no] = add_pos(rope[knot_no], (hmove, vmove))

            visited_tpos_pt2.add(rope[-1])

    
    print("Part 1: {}".format( len(visited_tpos) ) )
    print("Part 2: {}".format( len(visited_tpos_pt2) ) )
