import re

with open("input") as database:
    lines = database.readlines()

n_correct_passwords_pt1 = 0
n_correct_passwords_pt2 = 0

for line in lines:
    numbers = re.findall("\d+", line)

    # Part 1
    num1 = int(numbers[0])
    num2 = int(numbers[1])

    char = re.findall("[a-z]:", line)[0][:-1]

    password = line.split(":")[1].strip()
    
    n_chars = len(re.findall("{}".format(char), password))
    
    if num1 <= n_chars <= num2 :
        n_correct_passwords_pt1 = n_correct_passwords_pt1 + 1

    # Part 2
    if (password[num1 - 1] == char) ^ (password[num2 - 1] == char):
        n_correct_passwords_pt2 = n_correct_passwords_pt2 + 1

print("Part 1: {} correct passwords".format(n_correct_passwords_pt1))
print("Part 2: {} correct passwords".format(n_correct_passwords_pt2))
