# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self,name,room,age):
        self.name=name
        self.room=room
        self.age=age
        
    def __str__(self):
        return f"The player {self.name} belongs to {self.room} and is {self.age} old"