def bubble_sort(num_list, reverse=False):
    global result
    for _ in num_list:
        if reverse > 0:
            result = num_list[::-1]
        elif reverse < 0:
            result = num_list[::1]
        else:
            return num_list

    return result


print(bubble_sort([2, 5, 8, 6, 4, 2], 2))
