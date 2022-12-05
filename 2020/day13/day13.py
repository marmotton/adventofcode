import functools
import math

with open('input') as f:
    now = int(f.readline().strip())
    buses_raw = f.readline().strip().split(',')
    buses = [int(bus) for bus in buses_raw if bus is not 'x']

waiting_times = []

for bus in buses:
    next_departure = int(now / bus + 1) * bus
    waiting_times.append(next_departure - now)

waiting_time = min(waiting_times)
next_bus = buses[waiting_times.index(waiting_time)]

print("Part1: Next bus is {}, waiting time is {}. Answer = {}.".format(next_bus, waiting_time, next_bus*waiting_time))

# Part 2
offset = 0
offsets = []
for bus_or_x in buses_raw:
    if bus_or_x is not 'x':
        offsets.append(offset)

    offset -= 1  # Use negative starting offsets so we can find when all buses meet

def combined_bus(bus_a, bus_b):
    # Find when the two buses meet, this will be the offset of the combined bus
    timestamp = bus_a['offset']
    while (timestamp - bus_b['offset']) % bus_b['id'] != 0:
        timestamp += bus_a['id']

    # The id of the new bus will be the least common multiple of both buses
    new_bus = {'offset': timestamp, 'id': int(abs(bus_a['id'] * bus_b['id']) / math.gcd(bus_a['id'], bus_b['id']))}

    return new_bus

buses_with_offsets = [{'offset': offsets[i], 'id': buses[i]} for i in range(len(buses))]

# Combine all buses together
# The offset of the resulting bus corresponds to the timestamp we're looking for.
pt2_meet = functools.reduce(combined_bus, buses_with_offsets)

print("Part2: timestamp is {}".format(pt2_meet['offset']))
