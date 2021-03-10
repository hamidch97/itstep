def intersect(tup1: tuple, tup2: tuple, tup3: tuple) -> tuple:
    res = []
    for i in tup1:

        for j in tup2:
            if j == i:
                res.append(j)
            for k in tup3:
                if k == j:
                    res.append(k)
                if i == j == k:
                    res = [i, j, k]
    return tuple(set(res))


tup1 = (4, 2, 6, 7)
tup2 = (1, 2, 7, 2, 9)
tup3 = (2, 2, 2, 7, 1)

print(intersect(tup1, tup2, tup3))
