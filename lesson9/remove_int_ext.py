def remove_int(value_list):
    n = len(value_list)
    for num in value_list:
        value_list.remove(num)
        return value_list, n - len(value_list), "elements was deleded"


list_int = [2, 5, 4, 8, 3, 54, 25, 69]

print(remove_int(list_int))
