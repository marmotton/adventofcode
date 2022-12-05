import re

memory = {}
memory_pt2 = {}

mask_zeros = 0
mask_ones = 0
mask_x_bits = []

with open('input') as f:
    for line in f:
        if line[:4] == 'mask':
            pos = 35
            mask_ones = 0
            mask_zeros = 0
            mask_x_bits = []
            for b in line[7:].rstrip():
                if b == '0':
                    mask_zeros |= 1 << pos
                elif b == '1':
                    mask_ones |= 1 << pos
                elif b == 'X':
                    mask_x_bits.append(pos)
                pos -= 1

        if line[:3] == 'mem':
            params = re.split('[\[ \]=]', line.strip())
            
            addr = int(params[1])
            val = int(params[5])

            val |= mask_ones
            val &= ~mask_zeros

            memory[addr] = val

            # Part 2
            val = int(params[5])
            addr |= mask_ones

            for i in range(pow(2, len(mask_x_bits))):  # All the combinations of X
                addr_floating = addr
                for j in range(len(mask_x_bits)):  # set the X bits according to the current combination
                    if i & (1 << j) == 0:
                        addr_floating &= ~(1 << mask_x_bits[j])
                    else:
                        addr_floating |= 1 << mask_x_bits[j]

                memory_pt2[addr_floating] = val

    print("Part 1: sum is {}".format(sum(memory.values())))
    print("Part 2: sum is {}".format(sum(memory_pt2.values())))
