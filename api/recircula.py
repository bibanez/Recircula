import json
from tokenize import Double
from typing import List
from priority_queue_vec import Priority_queue as pq

path = "recipes.json"
with open(path) as file:
    recipes = json.load(file)

path = "ingredients.json"
with open(path) as file:
    ingredients = json.load(file)


def diff_score(v1: List, v2: List) -> float:
    s = 0
    t = 0
    for i in range(len(v1)-3):
        if v1[i] == 0 and v2[i] != 0:
            t += 1
        if v1[i] < v2[i]:
            s += (float(v1[i])-float(v2[i]))**2
    return s  # formula in terms of s and t


def missing_ingredients(my_recipe, recipe) -> List:
    missing_ingr = []
    for i in range(len(my_recipe)):
        dif = recipe[i]-my_recipe[i]
        if dif > 0:
            missing_ingr.append(dif)
        else:
            missing_ingr.append(0)
    return missing_ingr


def k_closest_recipes(recipe: List, recipes: List[List], k: int):
    for i in range(len(recipes)):
        recipes[i].append(diff_score(recipes[i], recipe))
    Q = pq(recipes)
    closest_k = []
    for i in range(k):
        closest_k.append(Q.remove_min())
    return closest_k


def scale_recipes(recipes: List[List], serving: float):
    for i in range(len(recipes)):
        for j in range(len(recipes[i])-3):
            if recipes[i][-1] != 0:
                recipes[i][j] *= serving/recipes[i][-1]


def exec(my_recipe: List, recipes: List[List], ingredients: List, k: int, serving: float):
    scale_recipes(recipes, serving)
    closest_k = k_closest_recipes(my_recipe, recipes, k)
    missing_k = []
    for j in range(k):
        missing_k.append(missing_ingredients(my_recipe, closest_k[j]))
    for i in range(len(closest_k)):
        print(closest_k[i][-3])
        for j in range(len(missing_k[i])):
            if missing_k[i][j] != 0:
                print("You are missing",
                      missing_k[i][j], "grams of", ingredients[j])


my_recipe = []
for i in range(len(ingredients)):
    if ingredients[i] in ['apples, raw, with skin', 'vanilla extract', 'yogurt, greek, plain, nonfat']:
        my_recipe.append(250)
    else:
        my_recipe.append(0)

exec(my_recipe, recipes, ingredients, 5, 100)
