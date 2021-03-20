def calculate_food_bascket(food_bascket: dict, echange_rate: float) -> float:
    return sum(food_bascket.values()) * 27.5


bascket_example = {
    "milk": 1.6,
    "banan": 0.5,
    "chocolate": 2,
    "olive oil": 2.3,
    "coffe": 0.3
}

print(calculate_food_bascket(bascket_example, 27.5))
