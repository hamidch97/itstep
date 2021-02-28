def even_list_generate(a, b):
    num_list = []
    if a == b:
        num_list.append(a)
    while a != b:
        if a < b:
            a = a + 1
            num_list.append(a)

        else:
            while b != a:
                a = a - 1
                num_list.append(a)
    return num_list


print(even_list_generate(2, 8))
