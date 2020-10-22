import pymongo

class MongoClient:
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = client["game_state"]
    mycol = mydb["game"]
    
    def save_game(self, p1_hand, p2_hand, p1_pts, p2_pts, deck, game_id, current_player)
        random_password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        game_state = { "p1_hand": p1_hand, "p2_hand": p2_hand, "player1_pts": p1_pts, 
            "player2_pts": p2_pts, "deck": deck, "game_id": game_id, "current_player": current_player,
            "pass_code": random_password}

        x = mycol.insert_one(game_state)
        print('inserted x')
        print(x)