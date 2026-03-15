from food import MainDish, Side, Snack, Drink  #Imports food classes

#stores the available food items
main_dishes = [
    MainDish("Pizza", 3, 285),
    MainDish("Pasta", 3, 320),
    MainDish("Ham Sandwich", 2, 200),
    MainDish("Tuna Sandwich", 2, 200),
    MainDish("Mac and Cheese", 3, 310),
    MainDish("Pickle, Turkey rollup", 1, 220),
]

sides = [
    Side("Chips", 2, 150),
    Side("Pretzels", 2, 110),
    Side("Popcorn", 3, 310),
    Side("Nuts", 1, 150),
]

snacks = [
    Snack("Apple", 1, 95),
    Snack("Banana", 2, 105),
    Snack("Granola Bar", 3, 115),
    Snack("Strawberries", 1, 105),
    Snack("Orange", 1, 75),
]

drinks = [
    Drink("Water", 1, 0),
    Drink("Soda", 3, 150),
    Drink("Chocolate Milk", 2, 115),
    Drink("Juice", 2, 100),
]