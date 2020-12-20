import re

my_ticket = []
nearby_tickets = []
rules = {}

with open('input') as f:
    file_section = "rules"

    for line_raw in f:
        line = line_raw.strip()
        
        # Find out which section of the file we're reading
        if "your ticket:" in line:
            file_section = "your ticket"

        elif "nearby tickets:" in line:
            file_section = "nearby tickets"

        # Read the content depending on which section we're in
        if file_section == "rules":
            rule = line.split(':')
            if len(rule) > 1:
                rule_name = rule[0]
                rules[rule_name] = [int(x) for x in re.findall("[0-9]+", rule[1])]

        elif file_section == "your ticket":
            ticket = line.split(',')
            if len(ticket) > 1:
                my_ticket = [int(val) for val in ticket]
        
        elif file_section == "nearby tickets":
            ticket = line.split(',')
            if len(ticket) > 1:
                nearby_tickets.append([int(val) for val in ticket])

scanning_error_rate = 0
valid_nearby_tickets = []  # For part 2

for ticket in nearby_tickets:
    ticket_is_valid = True
    for val in ticket:
        val_is_valid = False

        for rule in rules.values():
            if rule[0] <= val <= rule[1] or rule[2] <= val <= rule[3]:
                val_is_valid = True
                break

        if not val_is_valid:
            ticket_is_valid = False
            scanning_error_rate += val

    if ticket_is_valid:
        valid_nearby_tickets.append(ticket)

print("Part 1: scanning error rate is {}".format(scanning_error_rate))

# Part 2
# Apparently every rule could match a different number of fields
# --> Find the rule with only 1 matching field, remove this field, find the next rule which now has only 1 matching field etc.
def possible(rule_name, field_no):
    # Check that the values on the tickets match the rule
    for ticket in valid_nearby_tickets:
        if not (rules[rule_name][0] <= ticket[field_no] <= rules[rule_name][1] or rules[rule_name][2] <= ticket[field_no] <= rules[rule_name][3]):
            return False

    return True

# For every rule, list all the fields that could match
possible_fields = {k: [i for i in range(len(valid_nearby_tickets[0])) if possible(k, i)] for k in rules}

# Assign the correct field to each rule
rules_field_no = {k: None for k in rules}
loop = True
while loop:
    # Look for which rule has only 1 matching field and assign it
    for field_name, val in possible_fields.items():
        if len(val) == 1:
            rules_field_no[field_name] = val[0]
            # Remove the assigned field from the list of possible fields in every rule.
            # Another rule will now have only 1 matching field
            possible_fields = {k: [v for v in fields if v != val[0]] for k, fields in possible_fields.items()}
            break

    # Stop looping once possible_fields is empty
    loop = False
    for val in possible_fields.values():
        if len(val) > 0:
            loop = True
            break

# Multiply all the departure* fields of my ticket to get the answer
result = 1
for field_name, field_no in rules_field_no.items():
    if field_name.startswith('departure'):
        result *= my_ticket[field_no]

print("Part 2: result is {}".format(result))
