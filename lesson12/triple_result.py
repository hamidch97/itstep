def add(a, b):
    return a + b


add(5, 5)


def triple_result(func):
    def my_fun(a, b):
        print((a + b) * 3)

    return my_fun


@triple_result
def add(a, b):
    return a + b


add(5, 5)
