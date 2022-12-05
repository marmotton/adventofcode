import re

def bags_that_can_contain(my_bag_color):
    bags_that_can_contain_my_bag_color = {}
    for k, v in rules_dict.items():
        if my_bag_color in v:
            bags_that_can_contain_my_bag_color[k] = "x"

            for k1 in bags_that_can_contain(k):
                bags_that_can_contain_my_bag_color[k1] = "x"


    return bags_that_can_contain_my_bag_color


def my_bag_contains(my_bag_color):
    bags_contained_in_my_bag = {}
    for color, number in rules_dict[my_bag_color].items():
        bags_contained_in_my_bag[color] = bags_contained_in_my_bag.get(color, 0) + number

        for color1, number1 in my_bag_contains(color).items():
            bags_contained_in_my_bag[color1] = bags_contained_in_my_bag.get(color1, 0) + number1 * number
        
    return bags_contained_in_my_bag
    

with open("input") as f:
    rules = [line.split("bags contain") for line in f]

rules_dict = {}

for rule in rules:
    contained_bags = re.findall("[0-9]+ [a-z ]+ bag", rule[1])

    contained_bags_dict = {}
    for contained_bag in contained_bags:
        number = int(re.findall("[0-9]+", contained_bag)[0])
        color = contained_bag[int(number / 10)+2 : -4]

        contained_bags_dict[color] = number


    rules_dict[ rule[0].strip() ] = contained_bags_dict



print("Part 1: {} bags can contain a shiny gold bag".format(len(bags_that_can_contain("shiny gold"))))


number_of_bags_pt2 = 0
for k, v in my_bag_contains("shiny gold").items():
    number_of_bags_pt2 = number_of_bags_pt2 + v

print("Part 2: my shiny gold bag contains {} bags".format(number_of_bags_pt2))
