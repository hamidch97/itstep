def find_most_in_food_basket(food_bascket: dict, max_cost=True) -> list:
    res = []
    if max_cost:
        res.append(max(food_bascket, key=food_bascket.get))

    else:
        res.append(min(food_bascket, key=food_bascket.get))
    return res


big_bascket = {
    "milk": 1.6,
    "banan": 0.5,
    "chocolate": 2,
    "olive oil": 2.3,
    "coffe": 0.3,
    "beard": 0.3,
    "cheese": 2.3
}

print(find_most_in_food_basket(big_bascket))
