top_games={"counter strike2": 1100,
           "DOTA2": 571,
           "PUBG:Battlegrounds":334,
           "Rust": 123,
           "Delta Force": 106,
           "Banana": 104,
          "Phantom Blade Zero": 2000,
           "Stardew Valley": 8100}

largest = ""
for game in top_games.keys():
    current_game_players = top_games.get(game)
    largest_player_count = top_games.get(largest, 0)
    if current_game_players > largest_player_count:
        largest = game
print(f"{largest} had {top_games[largest]} thousands of players.")