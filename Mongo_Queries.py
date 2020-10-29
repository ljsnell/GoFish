import pymongo
import random
import string
import pickle

class MongoClient:
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = client["game_state"]
    game_col = mydb["game"]
    
    def save_game(self, p1_hand, p2_hand, p1_pts, p2_pts, deck, game_id, current_player):
        # Encode classes?
        pickle_hand1 = pickle.dumps(p1_hand)
        pickle_hand2 = pickle.dumps(p2_hand)
        pickle_deck = pickle.dumps(deck)
        # Game ID = # of documents in db + 1
        random_password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        game_state = { "p1_hand": pickle_hand1, "p2_hand": pickle_hand2, "player1_pts": p1_pts, 
            "player2_pts": p2_pts, "deck": pickle_deck, "game_id": game_id, "current_player": current_player,
            "pass_code": random_password}

        x = self.game_col.insert_one(game_state)
        print('inserted x')
        print(x)

    def retrieve_game(self, game_id): # Can add passcode next
        # https://www.w3schools.com/python/python_mongodb_find.asp
        game_state = self.game_col.find_one()
        print(game_state)
        print(pickle.loads(game_state['p1_hand']))
        # Use mongoDB compass.
        # C:\Program Files\MongoDB\Server\4.4\bin\mongod.exe