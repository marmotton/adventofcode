with open("input") as f:
    nums = [int(line) for line in f]

first_invalid_number = None

for i in range(25, len(nums)):
    current_num = nums[i]
    nums_before = nums[i-25:i]

    current_num_is_valid = False

    for n1 in nums_before:
        for n2 in nums_before:
            if n1 + n2 == current_num:
                current_num_is_valid = True
                break

        if current_num_is_valid:
            break

    if not current_num_is_valid:
        first_invalid_number = current_num
        break

print("Part 1: first invalid number is {}".format(first_invalid_number))

# Part 2
first_idx = 0
last_idx = 1

while True:
    s = sum(nums[first_idx:last_idx+1])

    if s == first_invalid_number:
        break

    elif s < first_invalid_number:
        last_idx = last_idx + 1

    elif s > first_invalid_number:
        first_idx = first_idx + 1

smallest = min(nums[first_idx:last_idx+1])
largest = max(nums[first_idx:last_idx+1])
print("Part 2: sum of the smallest and largest number in the range is {}".format(smallest + largest))
