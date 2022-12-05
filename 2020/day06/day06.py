with open("input") as f:
    all_answers = f.read()

group_answers = all_answers.split("\n\n")

total_count_yes_answers = 0

for group_answer in group_answers:
    answers = group_answer.replace("\n", "")

    total_count_yes_answers = total_count_yes_answers + len("".join(set(answers)))

print("Part 1: {} yes answers".format(total_count_yes_answers))

# Part 2

total_count_yes_answers_pt2 = 0

for group_answer in group_answers:
    individual_answers = group_answer.split()
    
    for c in range(ord('a'), ord('z')+1):
        char_is_in_each_answer = True
        for ans in individual_answers:
            if chr(c) not in ans:
                char_is_in_each_answer = False

        if char_is_in_each_answer:
            total_count_yes_answers_pt2 = total_count_yes_answers_pt2 + 1

print("Part 2: {} yes answers".format(total_count_yes_answers_pt2))
