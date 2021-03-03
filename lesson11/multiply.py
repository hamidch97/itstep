from functools import reduce

num_list = [1, 2, 5, 8, 7, 15, 48, 98, 97]
result = reduce(lambda x, y: x * y, num_list)
print(result)
