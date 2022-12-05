import time

def get_last_number(initial_numbers, target):
    already_spoken = {}
    previous_number = 0
    idx = 0

    # Store the last number
    previous_number = initial_numbers[-1]

    # Store the other numbers as already spoken
    for n in initial_numbers[:-1]:
        already_spoken[n] = idx
        idx += 1

    idx += 1  # Advance iterator by 1 to account for the number that was placed in previous_number

    while idx < target:
        if previous_number in already_spoken:
            age = (idx - 1) - already_spoken[previous_number]
            already_spoken[previous_number] = idx - 1
            previous_number = age
        else:
            already_spoken[previous_number] = idx - 1
            previous_number = 0

        idx += 1

    return previous_number


def get_last_number_faster(initial_numbers, target):
    already_spoken = [-1] * target
    previous_number = 0
    idx = 0

    # Store the last number
    previous_number = initial_numbers[-1]

    # Store the other numbers as already spoken
    for n in initial_numbers[:-1]:
        already_spoken[n] = idx
        idx += 1

    idx += 1  # Advance iterator by 1 to account for the number that was placed in previous_number

    while idx < target:
        if already_spoken[previous_number] != -1:
            age = (idx - 1) - already_spoken[previous_number]
            already_spoken[previous_number] = idx - 1
            previous_number = age
        else:
            already_spoken[previous_number] = idx - 1
            previous_number = 0

        idx += 1

    return previous_number


numbers = [9,6,0,10,18,2,1]
t0 = time.time()
result_pt1 = get_last_number(numbers, 2020)
t1 = time.time()
result_pt2 = get_last_number(numbers, 30000000)
t2 = time.time()
result_pt2_fast = get_last_number_faster(numbers, 30000000)
t3 = time.time()

print("Part1: 2020th number is {}. Computation time: {:.2f}ms.".format(result_pt1, (t1-t0)*1000))
print("Part2: 30000000th number is {}. Computation time: {:.2f}s.".format(result_pt2, t2-t1))
print("Part2: 30000000th number is {}. Computation time: {:.2f}s.".format(result_pt2_fast, t3-t2))
