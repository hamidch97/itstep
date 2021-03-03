string_list = ["1,2,3,4,5,6,7,8,9,6"]
num_list = map(filter(lambda x: x if int else None, string_list), string_list)
print(list(num_list))
