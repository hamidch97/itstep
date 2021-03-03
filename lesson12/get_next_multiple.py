def get_next_multiple(func):
    def source_fun(*a):
        b= a*2
        while a!=0:
             b = a
        return func(*a)
    return source_fun




gen_multiple_of_two = get_next_multiple(2)
print(next(gen_multiple_of_two))
print(next(gen_multiple_of_two))
