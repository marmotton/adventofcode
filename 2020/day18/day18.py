import re
from pprint import pprint

expressions = []

with open('input') as f:
    for line in f:
        new_expr = re.findall("[0-9]+|[+*()]", line)
        expressions.append(new_expr)

def solve(expr, part_no):
    stack = []
    operator = None
    operator_age = 0
    i = 0
    while i < len(expr):
        if expr[i] in ["+", "*"]:
            operator = expr[i]
            operator_age = 0

        elif expr[i] == "(":
            # Find matching parenthesis
            open_parentheses_count = 0
            matching_parenthesis_pos = 0
            for j in range(i, len(expr)):
                if expr[j] == "(":
                    open_parentheses_count += 1
                elif expr[j] == ")":
                    open_parentheses_count -= 1

                if open_parentheses_count == 0:
                    matching_parenthesis_pos = j
                    break

            # Recursively solve what is inside the parentheses
            stack.insert(0, solve(expr[i+1:matching_parenthesis_pos], part_no))
            operator_age += 1

            # Skip to the matching parenthesis as the content has been solved
            i = matching_parenthesis_pos

        elif expr[i] == ")":
            pass

        else:  # Number
            stack.insert(0, int(expr[i]))
            operator_age += 1

        if part_no == 1:  # Puzzle part 1
            if len(stack) == 2:
                if operator == "+":
                    stack[0] += stack.pop()
                elif operator == "*":
                    stack[0] *= stack.pop()
                operator = None

        else:  # Puzzle part 2
            if len(stack) > 1 and operator == "+" and operator_age > 0:  # Do the additions first
                stack[0] += stack.pop(1)
                operator = None
            
            if i == len(expr) - 1:  # Multiply all values remaining on the stack before returning
                for j in range(1, len(stack)):
                    stack[0] *= stack[j]

        i += 1

    return stack[0]


result_pt1 = 0
result_pt2 = 0
for expr in expressions:
    r1 = solve(expr, 1)
    r2 = solve(expr, 2)
    result_pt1 += r1
    result_pt2 += r2

print("Part 1: sum is {}".format(result_pt1))
print("Part 2: sum is {}".format(result_pt2))
