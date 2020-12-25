foods = []
with open("input") as f:
    for line in f:
        ingredients = line.split("(contains ")[0].split()
        allergens = line.rstrip(")\n").split("(contains ")[1].split(", ")
        foods.append({"ingredients": set(ingredients), "allergens": set(allergens)})

allergen_to_ingredient = {}
for food in foods:
    # Find out which ingredient might contain which allergen
    for allergen in food['allergens']:
        if allergen in allergen_to_ingredient:
            # This allergen is already in the dict
            # remove the ingredients that are not present in the current food
            ingredients_already_in_current_allergen = allergen_to_ingredient[allergen].copy()
            for ingredient in ingredients_already_in_current_allergen:
                if ingredient not in food['ingredients']:
                    allergen_to_ingredient[allergen].remove(ingredient)
        else:
            # This allergen is not in the dict yet
            # initilize it with all the ingredients of the current food
            allergen_to_ingredient[allergen] = food["ingredients"].copy()

ingredients_with_allergens = {ingredient for ingredients in allergen_to_ingredient.values() for ingredient in ingredients}

ingredient_without_allergens_count = 0
for food in foods:
    for ingredient in food['ingredients']:
        if ingredient not in ingredients_with_allergens:
            ingredient_without_allergens_count += 1

print("Part 1: {} ingredients without allergens".format(ingredient_without_allergens_count))

# Part 2
allergen_to_unique_ingredient = allergen_to_ingredient.copy()

done = False
while not done:
    done = True
    for allergen, ingredients in allergen_to_unique_ingredient.items():
        # If only 1 ingredient is listed, then we're sure that this ingredient contains the current allergen
        # We can therefore remove this ingredient from all the other allergens
        if len(ingredients) == 1:
            ingredient = list(ingredients)[0]
            for allergen2 in allergen_to_unique_ingredient:
                if allergen2 != allergen:
                    allergen_to_unique_ingredient[allergen2].discard(ingredient)
        else:
            # Try again until each allergen has only one ingredient
            done = False

# Use the alphabetical order of the allergens to sort the ingredients
sorted_allergens = list(allergen_to_unique_ingredient)
sorted_allergens.sort()
sorted_ingredients = [list(ingredient)[0] for allergen in sorted_allergens for ingredient in allergen_to_unique_ingredient.values() if allergen_to_unique_ingredient[allergen] == ingredient]

print("Part 2: dangerous ingredients are {}".format(",".join(sorted_ingredients)))
