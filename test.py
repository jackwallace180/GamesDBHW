from game_class import *
from database_class import *

conn_db =database( 'localhost,1433', 'GamesMarketplaceHW', 'SA', 'Passw0rd2018')

conn_db.print_all_games()

conn_db.delete_game('jack')