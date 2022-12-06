def detect_packet(data, length):
    for i in range(len(data) - length):
        unique_chars = { c for c in line[i:i+length] }  # Could also be written set(line[i:i+length])

        if len(unique_chars) == length:
            return i + length

    return 0
    

with open('input') as input:
    line = input.readline().strip()

    print("Part 1: {}".format( detect_packet(line, 4) ) )
    print("Part 2: {}".format( detect_packet(line, 14) ) )
