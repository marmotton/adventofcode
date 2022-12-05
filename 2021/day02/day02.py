with open('input') as input_file:
    text = input_file.read()

commands = [{'direction': c.split(' ')[0], 'value': int(c.split(' ')[1])} for c in text.split("\n") if len(c.split(' ')) > 1]

# Part 1: compute horizontal and depth positions based on up/down/forward commands

position = {'horizontal': 0, 'depth': 0}

for c in commands:

    if c['direction'] == 'forward':
        position['horizontal'] += c['value']

    elif c['direction'] == 'up':
        position['depth'] -= c['value']

    elif c['direction'] == 'down':
        position['depth'] += c['value']

answer = position['horizontal'] * position['depth']

print("Final position: h={}, d={}, h*d={}".format(position['horizontal'], position['depth'], answer))

# Part 2: Add an "aim". Down increases aim, Up decreases aim, Forward increases horizontal, Forward also increases depth by aim*value

position = {'horizontal': 0, 'depth': 0}
aim = 0

for c in commands:

    if c['direction'] == 'down':
        aim += c['value']

    elif c['direction'] == 'up':
        aim -= c['value']

    elif c['direction'] == 'forward':
        position['horizontal'] += c['value']
        position['depth'] += aim * c['value']

answer = position['horizontal'] * position['depth']

print("Part 2: Final position: h={}, d={}, h*d={}".format(position['horizontal'], position['depth'], answer))
