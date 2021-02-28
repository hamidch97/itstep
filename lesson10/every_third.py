from even_list_generate import even_list_generate as even


def every_third(even, step=3):
    result = []
    for i in even:
        result += step
    return result


every_third(even)
