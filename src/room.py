# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def _init_(self , name, description):
        self.name = name 
        self.description = description

    def _str_(self):
        return f"welcome to the {self.name}"