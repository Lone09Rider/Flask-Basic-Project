import json
import os

class Database:
    def insert(self, name, email, password):
        if not os.path.exists('users.json'):
            with open('users.json', 'w') as file:
                json.dump({}, file)
        
        with open('users.json', 'r') as file:
            users = json.load(file)
        
        if email in users:
            return 0
        else:
            users[email] = [name, password]
            with open('users.json', 'w') as file:
                json.dump(users, file, indent=4)
                return 1
            
    def login(self, email, password):
        with open('users.json', 'r') as file:
            users = json.load(file)
            
        if email in users:
            if users[email][1] == password:
                return users[email][0]  # Return the user's name
            else:
                return None
        else:
            return None