'''
 Problem;
Object Oriented Design -
Design a coffee maker machine class There is a coffee maker with a screen. We need to add three ingredients into the machine: coffee beans, water and milk.
There are three types of drinks we can make, below are the default recipes:
Espresso: cost 3 coffee beans and 1 water
Americano: cost 2 coffee beans and 3 water
Latte: cost 2 coffee beans, 2 milk and 2 water

When a user comes, on the screen we show available drinks. After the user chooses a drink, the user will be able to customize the amount of ingredients. (For example, after choosing Espresso, the user can change from default to 4 coffee beans and 1 water)
The admin is able to refill the ingredients. The admin and the users interact with the machine via the screen. In the future, we might can support more drink types.
Please design a class with public APIs to represent the coffee maker, which will be called by the screen. 
'''


class Ingredient:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def refill(self, amount):
        self.quantity += amount

    def use(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
        else:
            raise ValueError(f"Not enough {self.name} to make the drink.")


class DrinkRecipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def make_drink(self, coffee_maker):
        for ingredient, amount in self.ingredients.items():
            ingredient.use(amount)


class CoffeeMaker:
    def __init__(self):
        self.coffee_beans = Ingredient("coffee beans", 0)
        self.water = Ingredient("water", 0)
        self.milk = Ingredient("milk", 0)
        self.drink_recipes = {
            "Espresso": DrinkRecipe("Espresso", {"coffee_beans": 3, "water": 1, "milk": 0}),
            "Americano": DrinkRecipe("Americano", {"coffee_beans": 2, "water": 3, "milk": 0}),
            "Latte": DrinkRecipe("Latte", {"coffee_beans": 2, "water": 2, "milk": 2})
        }

    def refill_ingredients(self, coffee_beans, water, milk):
        self.coffee_beans.refill(coffee_beans)
        self.water.refill(water)
        self.milk.refill(milk)

    def make_drink(self, drink_name):
        if drink_name in self.drink_recipes:
            self.drink_recipes[drink_name].make_drink(self)
            return f"Here is your {drink_name}!"
        else:
            return "Sorry, this drink is not available."

    def get_available_drinks(self):
        available_drinks = []
        for drink_name, recipe in self.drink_recipes.items():
            try:
                recipe.make_drink(self)
                available_drinks.append(drink_name)
            except ValueError:
                pass
        return available_drinks

====================================================================

+---------------+
|  CoffeeMaker  |
+---------------+
| - coffee_beans: Ingredient
| - water: Ingredient
| - milk: Ingredient
| - drink_recipes: {DrinkRecipe}
| + refill_ingredients(coffee_beans, water, milk)
| + make_drink(drink_name)
| + get_available_drinks()
+---------------+

+---------------+
|  Ingredient   |
+---------------+
| - name: string
| - quantity: int
| + refill(amount)
| + use(amount)
+---------------+

+---------------+
|  DrinkRecipe  |
+---------------+
| - name: string
| - ingredients: {Ingredient: int}
| + make_drink(coffee_maker)
+---------------+

=================================== TEST CASES =================================

import unittest
from coffee_maker import CoffeeMaker, Ingredient, DrinkRecipe

def test_refill_ingredients():
    coffee_maker = CoffeeMaker()
    coffee_maker.refill_ingredients(10, 10, 10)
    assert coffee_maker.coffee_beans.quantity == 10
    assert coffee_maker.water.quantity == 10
    assert coffee_maker.milk.quantity == 10

def test_make_drink_espresso():
    coffee_maker = CoffeeMaker()
    coffee_maker.refill_ingredients(10, 10, 10)
    assert coffee_maker.make_drink("Espresso") == "Here is your Espresso!"
    assert coffee_maker.coffee_beans.quantity == 7
    assert coffee_maker.water.quantity == 9
    assert coffee_maker.milk.quantity == 10

def test_make_drink_latte():
    coffee_maker = CoffeeMaker()
    coffee_maker.refill_ingredients(10, 10, 10)
    assert coffee_maker.make_drink("Latte") == "Here is your Latte!"
    assert coffee_maker.coffee_beans.quantity == 8
    assert coffee_maker.water.quantity == 8
    assert coffee_maker.milk.quantity == 8

def test_not_enough_ingredients():
    coffee_maker = CoffeeMaker()
    coffee_maker.refill_ingredients(2, 2, 2)
    assert coffee_maker.make_drink("Latte") == "Sorry, not enough resources to make the drink."

def test_available_drinks():
    coffee_maker = CoffeeMaker()
    coffee_maker.refill_ingredients(10, 10, 10)
    assert "Espresso" in coffee_maker.get_available_drinks()
    assert "Americano" in coffee_maker.get_available_drinks()
    assert "Latte" in coffee_maker.get_available_drinks()

def test_custom_recipe():
    coffee_maker = CoffeeMaker()
    coffee_maker.refill_ingredients(10, 10, 10)
    custom_recipe = DrinkRecipe("Custom", {"coffee_beans": 4, "water": 3, "milk": 2})
    coffee_maker.drink_recipes["Custom"] = custom_recipe
    assert coffee_maker.make_drink("Custom") == "Here is your Custom!"
    assert coffee_maker.coffee_beans.quantity == 6
    assert coffee_maker.water.quantity == 7
    assert coffee_maker.milk.quantity == 8

if __name__ == '__main__':
    unittest.main()
