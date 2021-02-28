import random


def mu_fonc():
    random_numbers = [random.randrange(1, 100, 1) for _ in range(100)]
    new_list = []
    for i in range(len(random_numbers)):
        if random_numbers[i] < 10:
            new_list = new_list + [random_numbers[i]]

    return new_list


print(mu_fonc())
