"""
Meal Selector
This program will help users create a meal based on pre-defined choices.
Created by Michael Drake - 03/15/26
"""

import random
from datetime import datetime

#imports necessary files to run program fully
from meal import Meal
from data import main_dishes, sides, snacks, drinks

#creates a log file for future reference
LOG_FILE = "past_choices.txt"

#obtains user input
def get_hunger_level():
    valid = False
    while not valid:
        print("\nHow Hungry are you?")
        print("1 = I'm kinda hungry")
        print("2 = I'm Hungry")
        print("3 = I'm STARVING!")

        try:
            level = int(input("Enter hunger level(1-3):"))
            if level >=1 and level <= 3:
                return level
            else:
                print("Please enter 1, 2, or 3")

        except ValueError:
            print("Error: Please ask an adult for help")

    return level

#chooses random foods based on users hunger level
def choose_food(food_list, hunger_level):
    matches = [food for food in food_list if food.hunger_level <= hunger_level]
    return random.choice(matches) if matches else None

#saves chosen foods to log file
def save_to_file(hunger_level, meal):
    timestamp = datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")
    food_names=",".join(food.name for food in meal.food_list())

    with open(LOG_FILE, "a") as file:
        file.write(
            f"{timestamp} | Hunger Level:{hunger_level} |"
            f"Meal:{food_names} | Calories:{meal.total_calories()}\n"
        )

#main program logic
def main():
    hunger=get_hunger_level()
    running= True

    while running:
        main_food=choose_food(main_dishes, hunger)
        side=choose_food(sides, hunger)
        snack=choose_food(snacks, hunger)
        drink=choose_food(drinks, hunger)

        meal=Meal(main_food, side, snack, drink)

        print(meal)

        print("\nOptions:")
        print("1 = I don't want to eat this")
        print("2 = Change hunger level")
        print("3 = I want to eat this")

        choice = input("Enter your choice(1-3): ")
        if choice == "1":
            pass
        elif choice == "2":
            hunger=get_hunger_level()
        elif choice == "3":
            save_to_file(hunger, meal)
            print("Good Choice, please ask an adult for help!")
            running=False

        else:
            print("Please enter 1, 2, or 3")

if __name__ == "__main__":
    main()

