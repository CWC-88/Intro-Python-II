# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def _init_(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom

    def _str_(self):
        return f'{self.name} is in the {self.currentRoom}'

