import re
import time

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

t0 = time.time()
valid_messages = set(generate_messages(0))

n_valid_messages = 0

for message in messages:
    if message in valid_messages:
        n_valid_messages += 1

t1 = time.time()
print("Part 1: {} valid messages. Verification time {:.2f}s".format(n_valid_messages, t1 - t0))

# Using regex
def generate_regex(rule_no):
    if isinstance(rules[rule_no][0], str):
        regex = rules[rule_no][0]

    else:
        if len(rules[rule_no]) > 1:
            regex = "("
        else:
            regex = ""

        # Generate all parts of the OR
        for rule in rules[rule_no]:
            for num in rule:
                regex += generate_regex(num)
            regex += "|"

        # Remove the last |
        regex = regex[:-1]

        if len(rules[rule_no]) > 1:
            regex += ")"

    return regex

t2 = time.time()

n_valid_messages = 0
big_regex = re.compile(generate_regex(0))
for message in messages:
    if big_regex.fullmatch(message):
        n_valid_messages += 1

t3 = time.time()

print("Part 1 using regex: {} valid messages. Verification time {:.2f}s".format(n_valid_messages, t3 - t2))


# Part 2
# Instead of an infinite loop, generate some more options for rules 8 and 11.
# The upper value of the range() is set by 
for i in range(2, 10):
    rules[8].append([42] * i)

for i in range(2, 10):
    rules[11].append([42] * i + [31] * i)


t4 = time.time()

n_valid_messages = 0
big_regex = re.compile(generate_regex(0))

for message in messages:
    if big_regex.fullmatch(message):
        n_valid_messages += 1

t5 = time.time()

print("Part 2 using regex: {} valid messages. Verification time {:.2f}s".format(n_valid_messages, t5 - t4))
