import copy
import math

monkeys = []

with open('input') as input:
    current_monkey = {}

    for line in input:
        elems = line.strip().replace(', ', ':').replace(' ', ':').split(':')

        match elems:
            case ['Monkey', num, *rest]:
                current_monkey['num'] = int(num)
            case ['Starting', 'items', '', *items]:
                current_monkey['items'] = [int(x) for x in items]
            case ['Operation', *rest]:
                current_monkey['operation'] = ' '.join( rest[3:] )
            case ['Test', *rest]:
                current_monkey['test_divisible'] = int(rest[3])
            case ['If', 'true', *rest]:
                current_monkey['throw_to'] = [-1, int(rest[4])]
            case ['If', 'false', *rest]:
                current_monkey['throw_to'][0] = int(rest[4])
                current_monkey['n_inspections'] = 0
                monkeys.append(current_monkey.copy())

    monkeys_pt2 = copy.deepcopy(monkeys)  # Deepcopy as there are lists in the monkey dicts

    for _ in range(20):
        for monkey in monkeys:
            for item in monkey['items']:
                monkey['n_inspections'] += 1
                old = item
                new_worry_level = eval( monkey['operation'] ) // 3
                test_result = ( new_worry_level % monkey['test_divisible'] ) == 0
                throw_to = monkey['throw_to'][ test_result ]
                monkeys[throw_to]['items'].append(new_worry_level)
            
            monkey['items'] = []

    n_inspections = [x['n_inspections'] for x in monkeys]
    n_inspections.sort()
    print("Part 1: {}".format(n_inspections[-1] * n_inspections[-2]))

    # Part 2
    # math.prod() would get the same result as the numbers are prime
    common_multiple = math.lcm( *[x['test_divisible'] for x in monkeys_pt2] )  # '*' unpacks a list into arguments

    for _ in range(10000):
        for monkey in monkeys_pt2:
            for item in monkey['items']:
                monkey['n_inspections'] += 1
                old = item
                new_worry_level = eval( monkey['operation'] ) % common_multiple
                test_result = ( new_worry_level % monkey['test_divisible'] ) == 0
                throw_to = monkey['throw_to'][ test_result ]
                monkeys_pt2[throw_to]['items'].append(new_worry_level)

            monkey['items'] = []

    n_inspections = [x['n_inspections'] for x in monkeys_pt2]
    n_inspections.sort()
    print("Part 2: {}".format(n_inspections[-1] * n_inspections[-2]))
