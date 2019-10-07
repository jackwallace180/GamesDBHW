from game_class import *
from database_class import *

conn_db =database( 'localhost,1433', 'GamesMarketplaceHW', 'SA', 'Passw0rd2018')

print('Welcome to Games! Games? Games...')
input1 = int(input(
    'press 1 to list all games, 2 to find a game, 3 to add/delete a game, press 4 to update price, press 5 to exit '))
while True:
    if input1 == 1:
        conn_db.print_all_games()
        input1 = int(input('press 1 to list all games, 2 to find a game, 3 to add/delete a game, press 4 to update price, press 5 to exit '))

    elif input1 == 2:
        game = input('which game do you want to look up? (use name from table)')
        conn_db.print_a_game(game)
        input1 = int(input('press 1 to list all games, 2 to find a game, 3 to add/delete a game, press 4 to update price, press 5 to exit '))

    elif input1 == 3:
        result = input('do you want to add or delete a game to our database?').lower().strip()

        if result == 'add':
            game_name1 = input('what is the name of the game?')
            phone1 = input('what is your contact number?')
            price1 = input('what is the price you want to list the game for?')
            postcode1 = input('what is your postcode?')
            game1 = Game(game_name1, phone1, price1, postcode1)
            conn_db.add_game(game1)
            print('game added to our database!')
            input1 = int(input('press 1 to list all games, 2 to find a game, 3 to add/delete a game, press 4 to update price, press 5 to exit '))

        elif result == 'delete':
            game_name1 = input('what is the name of the game you want to delete? (as listed in DB)')
            conn_db.delete_game(game_name1)
            print('game has been deleted from our database')
            input1 = int(input('press 1 to list all games, 2 to find a game, 3 to add/delete a game, press 4 to update price, press 5 to exit '))

        else:
            print('not a valid input')
            input1 = int(input('press 1 to list all games, 2 to find a game, 3 to add/delete a game, press 4 to update price, press 5 to exit '))

    elif input1 == 4:
        game_name1 = input('what is the game you want to change the price for? (use name from DB)')
        conn_db.change_price(game_name1)
        print('price updated!')
        input1 = int(input(
            'press 1 to list all games, 2 to find a game, 3 to add/delete a game, press 4 to update price, press 5 to exit '))

    elif input1 == 5:
        print('thank you for using Games! Games? Games..., goodbye!')
        break

    else:
        print('this is not a valid input')
        input1 = int(input('press 1 to list all games, 2 to find a game, 3 to add/delete a game, press 4 to update price, press 5 to exit '))