import re

rules = {}
messages = []

with open("input") as f:
    for line in f:
        parts = line.strip().split(":")
        
        # Message (e.g. "aabaabbbaaba")
        if len(parts) == 1:
            if len(parts[0]) > 0:
                messages.append(parts[0])

        # Rule
        else:
            rule = []
            rule_no = int(parts[0])
            subrules = parts[1].split("|")

            for subrule in subrules:
                rule_nums = [int(n) for n in re.findall("[0-9]+", subrule)]

                if len(rule_nums) > 0:
                    rule.append(rule_nums)

                else:
                    rule_char = re.findall("[a-z]", subrule)

                    if len(rule_char) > 0:
                        rule.append(rule_char[0])
            
            rules[rule_no] = rule


def generate_messages(rule_no):
    if isinstance(rules[rule_no][0], str):
        messages = [rules[rule_no][0]]

    else:
        messages = []
        for rule in rules[rule_no]:

            messages_temp = []

            for r in rule:
                child_messages = generate_messages(r)

                if len(messages_temp) == 0:
                    messages_temp = child_messages.copy()

                else:
                    new_messages = []
                    for message in messages_temp:
                        for child_message in child_messages:
                            new_messages.append(message + child_message)

                    messages_temp = new_messages

            for new_msg in messages_temp:
                messages.append(new_msg)

    return messages


valid_messages = generate_messages(0)

n_valid_messages = 0

for message in messages:
    if message in valid_messages:
        n_valid_messages += 1

print("Part 1: {} valid messages".format(n_valid_messages))

# Part 2
rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]
