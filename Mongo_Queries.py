import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["game_state"]
mycol = mydb["game"]

mydict = { "p1_hand": "John", "p2_hand": "Highway 37", "player1_pts": "0", 
    "player2_pts": "0", "deck": "deck", "game_id": "1", "current_player": "Player 1", "pass_code": "random_password"}

x = mycol.insert_one(mydict)
print('inserted x')
print(x)
# p1_hand
# p2_hand
# player1_pts
# player2_pts
# deck
# game_id
# current_player