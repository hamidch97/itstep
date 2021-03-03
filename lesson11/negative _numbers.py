num_list = [1, 2, 5, -4, 8, -6, 7, 15, -11, 48, 98, -36, 97]
ressult = list(filter(lambda x: x if x >= 0 else None, num_list))
print(ressult)
