def only_odd_argements(fun):
    def source_fun(*a,**b):

            return fun(*a)

        else:
            print("add odd numbers please")

    return source_fun


@only_odd_argements
def add(a, b):
    return a + b


add(5, 5)

# @only_odd_argements
# def mltiply(a, b, c, d, e):
#     return a * b * c * d * e
#
#
# mltiply(1, 2, 3, 4, 5)
