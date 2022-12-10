import time

reg = 1
cycle = 1
signal_strength_sum = 0

# Image of part 2
image = [' ' * 40] * 6

def process():
    global signal_strength_sum

    if cycle in range(20, 221, 40):
        signal_strength_sum += cycle * reg

    # Part 2
    col = (cycle - 1) % len(image[0])
    row = (cycle - 1) // len(image[0])
    
    if reg -1 <= col <= reg + 1:
        image[row] = "{}▒{}".format( image[row][:col], image[row][col + 1:] )

with open('input') as input:
    for line in input:
        match line.strip().split():
            case ['noop']:
                process()
                cycle += 1

            case ['addx', val]:
                process()
                cycle += 1
                process()
                cycle += 1
                reg += int(val)
                

    print("Part 1: {}".format(signal_strength_sum))

    # Part 2 animated
    print("Part 2:")
    for row in image:
        for c in row:
            print(c, end='', flush=True)
            time.sleep(0.02)
        print()
