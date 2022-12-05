with open('input') as expenses:
    text = expenses.read()

numbers = [int(num) for num in text.split()]

for first in numbers:
    for second in numbers:
        if first + second == 2020:
            print("Part 1: {} * {} = {}".format(first, second, first*second))

        for third in numbers:
            if first + second + third == 2020:
                print("Part 2: {} * {} * {} = {}".format(first, second, third, first*second*third))
