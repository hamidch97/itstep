import random


def binary_search(num_list, item):
    begin_index = 0
    end_index = len(num_list) - 1
    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = num_list[midpoint]
        if midpoint_value == item:
            return midpoint
        elif item < midpoint_value:
            end_index = midpoint - 1
        else:
            end_index = midpoint + 1

    return None


list_numbers = [random.randrange(1, 100, 1) for i in range(11)]
print(list_numbers)
user = int(input("enter numbers here"))
print(binary_search(list_numbers, user))
