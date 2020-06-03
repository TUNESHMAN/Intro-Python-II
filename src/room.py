# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, width, colour):
        self.name=name
        self.width=width
        self.colour=colour
    def __str__(self):
        return f"The room ${self.name} has a width of {self.width} and a colour of ${self.colour}"
        