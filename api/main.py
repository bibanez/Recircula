from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

class IngredientList(BaseModel):
    ingredients: List[Ingredient]

class Ingredient(BaseModel):
    name: str
    weight: float


with open('ingredients.json') as file:
    _ingredients = json.load(file)

with open('recipes.json') as file:
    _recipes = json.load(file)

app = FastAPI()

@app.get("/ingredients")
async def ingredients():
    return _ingredients

@app.get("/recipes")
async def recipes(page: int = 1, maxResults: int = 20):
    return _recipes[(page-1)*maxResults:page*maxResults]

@app.get("/recipe/{recipe_id}")
async def recipe(recipe_id: int):
    return _recipes[recipe_id]

@app.put("/recommendation")
async def recommendation(ingredients: IngredientList):

