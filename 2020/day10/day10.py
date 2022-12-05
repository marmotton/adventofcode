with open("input") as f:
    adapters = [int(line) for line in f]

adapters.sort()
adapters.insert(0, 0)  # Outlet 0-jolts
adapters.append(max(adapters) + 3)  # Builtin adapter, 3-jolts above max

jolts_diffs = [0, 0, 0]
for i in range(1, len(adapters)):
    diff = adapters[i] - adapters[i-1]

    jolts_diffs[diff-1] = jolts_diffs[diff-1] + 1

print("Part 1: {} 1-jolt * {} 3-jolt = {}".format(jolts_diffs[0], jolts_diffs[2], jolts_diffs[0] * jolts_diffs[2]))

# Part 2 (thanks https://www.reddit.com/r/adventofcode/comments/kacdbl/2020_day_10c_part_2_no_clue_how_to_begin/)
# Find how many paths can lead to every adapter in the chain, starting from the outlet
paths = [1] + [0] * (len(adapters) - 1)
for i in range(len(adapters)):
    for j in range(1,4):
        if (i+j) < len(adapters) and adapters[i+j] - adapters[i] <= 3:
            paths[i+j] += paths[i]

print("Part 2: {} possible adapters combinations".format(paths[-1]))
