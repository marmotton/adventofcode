with open('input') as input_file:
    text = input_file.read()

depths = [int(d) for d in text.split()]

# Part 1: count how many times the depth value increases compared to the previous one
n_increases = 0

for i in range(1, len(depths)):
    if depths[i] > depths[i-1]:
        n_increases += 1

print("The depth reading increased {} times.".format(n_increases))

# Part 2: same thing but using the sum of a 3-values sliding window
n_increases = 0

for i in range(1, len(depths) - 2):
    sum_current = depths[i] + depths[i+1] + depths[i+2]
    sum_previous = depths[i-1] + depths[i] + depths[i+1]

    if sum_current > sum_previous:
        n_increases += 1

print("The depth reading increased {} times (using a 3-value sliding window).".format(n_increases))
