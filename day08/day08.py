import copy

def execute_program(c):
    executed_lines = []
    accumulator = 0
    current_line = 0
    terminated_normally = False

    while current_line not in executed_lines:
        instruction = c[current_line][0]
        parameter = int(c[current_line][1])
        executed_lines.append(current_line)

        if instruction == "nop":
            current_line = current_line + 1

        elif instruction == "jmp":
            current_line = current_line + parameter

        elif instruction == "acc":
            current_line = current_line + 1
            accumulator = accumulator + parameter

        if current_line == len(code):
            terminated_normally = True
            break

    return accumulator, terminated_normally


with open("input") as f:
    code = [line.split() for line in f]


# Part 1
acc, __ = execute_program(code)
print("Part 1: accumulator value is {} before starting the infinite loop".format(acc))

# Part 2
for i in range(len(code)):
    new_code = copy.deepcopy(code)

    if new_code[i][0] == "nop":
        new_code[i][0] = "jmp"

    elif new_code[i][0] == "jmp":
        new_code[i][0] = "nop"

    else:
        continue

    acc, terminated_normally = execute_program(new_code)

    if terminated_normally:
        print("Part 2: program terminated normally, accumulator value is {}".format(acc))
        break
