from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from recircula import recommend, ingredients_to_vector
import json

class Ingredient(BaseModel):
    name: str
    weight: float

class IngredientList(BaseModel):
    servings: float
    maxResults: int
    ingredients: List[Ingredient]

with open('../Sources/ingredients.json') as file:
    _ingredients = json.load(file)

with open('../Sources/recipes.json') as file:
    _recipes = json.load(file)

with open('../Sources/pretty_recipes.json') as file:
    _pretty_recipes = json.load(file)

app = FastAPI()

@app.get("/ingredients")
async def ingredients():
    return _ingredients

@app.get("/recipes")
async def recipes(page: int = 1, maxResults: int = 20):
    i = (page-1)*maxResults
    j = page*maxResults
    res = {}
    for x in list(_pretty_recipes)[i:j]:
        res[x] = _pretty_recipes[x]
    
    return res

@app.get("/recipe/{recipe_id}")
async def recipe(recipe_id: str):
    return _pretty_recipes[recipe_id]

@app.put("/recommendation")
async def recommendation(ingr: IngredientList | None = None):
    if ingr:
        my_recipe = ingredients_to_vector(ingr["ingredients"])
        return recommend(my_recipe, _recipes, _ingredients, ingr["maxResults"], ingr["servings"])

    return None
