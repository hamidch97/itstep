import json
import pickle

shopping_list_example = [
    {
        'bread': 1.2,
        'milk': 1.6,
        'potato': 0.4,
        'sunflower oil': 2,
        'meat': 2.4
    },
    {
        'bread': 1.2,
        'milk': 1.6,
        'potato': 0.4,
        'sunflower oil': 2,
        'meat': 2.4,
        'eggs': 0.4,
        'fish': 2.4
    }
]
with open('shopping_list_example.pickle', 'wb') as f:
    print(pickle.dumps(shopping_list_example))

with open('shopping_list_example.json', 'wb') as f:
    print(json.dumps(shopping_list_example))
