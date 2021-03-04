def only_odd_argements(fun):
    def source_fun(*a, **b):
        for i in a:
            if i % 2 != 0:
                return fun(*a, **b)
        for i in a:
            if i % 2 != 0:
                return fun(*a, **b)

        else:
            print("add odd numbers please")

    return source_fun


@only_odd_argements
def add(a, b):
    return a + b


add(4, 4)


@only_odd_argements
def mltiply(a, b, c, d, e):
    return a * b * c * d * e


print(mltiply(2, 2, 3, 4, 5))
