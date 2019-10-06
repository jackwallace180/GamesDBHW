from game_class import *
from database_class import *

conn_db =database( 'localhost,1433', 'GamesMarketplaceHW', 'SA', 'Passw0rd2018')

Wii_sports = game('Wii sports','013345678','£70','DA157JQ')

print(game.long_find(Wii_sports))

# conn_db.add_game(Wii_sports)
print(conn_db.search_for_a_game('wii sports'))


input1 = int(input(
    'press 1 to list all games, 2 to find a game, 3 to add/delete a game, 4 to look up an ingredient, 5 to find a recipe postcode constituency, press 6 to exit '))
while True:
    if input1 == 1:
        conn_db.print_all_recipes()
        input1 = int(input('press 1 to list all recipes, 2 to find an individual recipe, 3 to add/delete a recipe, 4 to look up an ingredient, 5 to find a recipe postcode info, press 6 to exit '))

    elif input1 == 2:
        recipe = input('which recipe do you want to see?')
        print(conn_db.search_recipe(recipe))
        input1 = int(input(
            'press 1 to list all recipes, 2 to find an individual recipe, 3 to add/delete a recipe, 4 to look up an ingredient, 5 to find a recipe postcode info, press 6 to exit '))

    elif input1 == 3:
        result = input('do you want to add or delete a recipe?')
        if result == 'add':
            recipe_name = input('what is the name of the recipe?')
            ingredients = input('what are the ingredients?')
            method = input('what is the method?')
            postcode = input('what is the postcode?')
            conn_db.add_recipe(recipe_name, ingredients, method, postcode)
            input1 = int(input(
                'press 1 to list all recipes, 2 to find an individual recipe, 3 to add/delete a recipe, 4 to look up an ingredient, 5 to find a recipe postcode info, press 6 to exit '))
        elif result == 'delete':
            recipe_name = input('what is the name of the recipe you want to delete?')
            conn_db.delete_recipe(recipe_name)
            print('recipe has been deleted')
            input1 = int(input(
                'press 1 to list all recipes, 2 to find an individual recipe, 3 to add/delete a recipe, 4 to look up an ingredient, 5 to find a recipe postcode info, press 6 to exit '))
        else:
            print('not a valid input')
            input1 = int(input(
                'press 1 to list all recipes, 2 to find an individual recipe, 3 to add/delete a recipe, 4 to look up an ingredient, 5 to find a recipe postcode info, press 6 to exit '))
