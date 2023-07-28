

valid_bread_types = {
    "baguette",
    "tiger bread",
    "sourdough",
}


valid_ingredients = {
    "tomato",
    "lettuce",
    "cheese",
    "onions",
}


def make_sandwich(bread, ingredients):
    """
    Ask to make a type of sandwich
    """

    sandwich = []

    if bread in valid_bread_types:
        print(f"Using {bread}")
        sandwich.append(bread)
    
    else:
        raise ValueError("We don't have this kind of bread")

    for i in range(len(ingredients)):
        ingredient = ingredients[i]
        if ingredient in valid_ingredients:
            print(f"Using {ingredient}")
            sandwich.append(ingredient)

        else:
            raise ValueError(f"We dont have this ingredient: {i}")

    sandwich.append(bread)

    return sandwich


result = make_sandwich("sourdough", ["cheese", "tomato"])
print(result)
