import re

import json
from typing import List, Dict

path = "recipes_with_nutritional_info.json"

with open(path) as file:
    data = json.load(file)

#quantity = int(input("How many grams of food do you want to eat?"))

ingredients = []


def scale_recipe(recipe, quantity, total_weight) -> List:
    scaled_recipe = []
    for i in range(len(recipe)):
        scaled_recipe.append(recipe[i]*quantity/total_weight)
    return scaled_recipe


for i in range(len(data)):
    for j in range(len(data[i]['ingredients'])):
        if data[i]['ingredients'][j]['text'] not in ingredients:
            ingredients.append(data[i]['ingredients'][j]['text'])

ingredients.sort()

save_path = "ingredients.json"
with open(save_path, 'w') as file:
    json.dump(ingredients, file)

recipes = [[] for i in range(len(data))]

for i in range(len(data)):
    recipe_ingr = []
    for k in range(len(data[i]['ingredients'])):
        recipe_ingr.append(data[i]['ingredients'][k]['text'])
    l = 0
    for j in range(len(ingredients)):
        total_weight = 0
        if ingredients[j] in recipe_ingr:
            recipes[i].append(data[i]['weight_per_ingr'][l])
            total_weight += data[i]['weight_per_ingr'][l]
            l += 1
        else:
            recipes[i].append(0)
    #recipes[i] = scale_recipe(recipes[i], quantity, total_weight)
    recipes[i].append(data[i]['id'])  # add whatever info we need.
    recipes[i].append(data[i]['title'])
    recipes[i].append(total_weight)

save_path = "recipes.json"
with open(save_path, 'w', encoding='utf-8') as file:
    print("Generating json...")
    json.dump(recipes, file, ensure_ascii=False, indent=4)
