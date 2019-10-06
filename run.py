from game_class import *
from database_class import *

conn_db =database( 'localhost,1433', 'GamesMarketplaceHW', 'SA', 'Passw0rd2018')

Wii_sports = game('Wii sports','013345678','£70','DA157JQ')

print(game.long_find(Wii_sports))

# conn_db.add_game(Wii_sports)

print(conn_db.search_for_a_game('wii sports'))

