class Meal:

    def __init__(self,main,side,snack,drink):
        self.main=main
        self.side=side                        #Creates a meal using multiple foods
        self.snack=snack
        self.drink=drink

                                            #returns a list of foods that exist in the meal.
    def food_list(self):
        return [food for food in [self.main,self.side,self.snack,self.drink]if food]

                                            #returns total calories for the meal.
    def total_calories(self):
        return sum(food.calories for food in self.food_list())

                                            #formats how the text string appears when printing.
    def __str__(self):
        text="\nMeal Recommendation\n"
        text+="----------\n"
        if self.main:
            text+=f"Main Dish:{self.main}\n"
        if self.side:
            text+=f"Side:{self.side}\n"
        if self.snack:
            text+=f"Snack:{self.snack}\n"
        if self.drink:
            text+=f"Drink:{self.drink}\n"
        text+=f"\nTotal Calories:{self.total_calories()}"

        return text
