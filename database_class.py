import pyodbc
import requests
from game_class import *

class database():

        def __init__(self, server, database, username, password):
            self.server = server
            self.database = database
            self.username = username
            self.password = password
            self.conn_db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password + '')
            self.cursor = self.conn_db.cursor()

        def filter_query(self, query):
            return self.cursor.execute(query)

        def print_all_games(self):
            rows = self.filter_query("SELECT * FROM Games_db")
            while True:
                game = rows.fetchone()
                if game is None:
                    break
                print('Name: ', game.Game, ', contact number: ', game.Phone, ', Price : ', game.Price, ',Location : ', game.Postcode, game.Long, game.Lat)

        def add_game(self, game_name):
            longitude = game.long_find(game_name)
            latitude = game.lat_find(game_name)
            self.filter_query(f"INSERT INTO Games_db VALUES ('{game_name.name}','{game_name.phone}','{game_name.price}','{game_name.postcode}','{longitude}','{latitude}')")
            self.conn_db.commit()

        def delete_game(self, game_name):
            self.filter_query(f"DELETE FROM Games_db WHERE Game = '{game_name}'")
            self.conn_db.commit()

        def print_a_game(self, game_name):
            find_recipe = self.filter_query(f"SELECT * FROM Games_db WHERE Game = '{game_name}'")
            game = find_recipe.fetchone()
            print('Name: ', game.Game, ', contact number: ', game.Phone, ', Price : ', game.Price, ',Location : ', game.Postcode, game.Long, game.Lat)






        


