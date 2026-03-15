class Food:    #Parent class representing food items

    def __init__(self, name, hunger_level, calories):
    #protected attributes
     self._name = name
     self._hunger_level = hunger_level
     self._calories = calories

    @property
    def name(self):
        return self._name

    @property
    def hunger_level(self):                        #Getters for accessing each protected attribute
        return self._hunger_level

    @property
    def calories(self):
        return self._calories

    def __str__(self):
        return f"{self._name} | ({self.calories} calories)"

class MainDish(Food):
    pass

class Side(Food):
    pass                                     #Child classes inherit everything from Food class

class Snack(Food):
    pass
class Drink(Food):
    pass
