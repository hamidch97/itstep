def unique(tup1: tuple, tup2: tuple, tup3: tuple) -> tuple:
    res = []
    for i in tup1:
        if i not in tup2 and i not in tup2:
            res.append(i)
        for j in tup2:
            if j not in tup1 and j not in tup3:
                res.append(j)
            for k in tup3:
                if k not in tup1 and k not in tup2:
                    res.append(k)
    return tuple(set(res))


tup1 = (4, 2, 6, 7)
tup2 = (1, 2, 7, 2, 9)
tup3 = (2, 2, 2, 7, 1)
print(unique(tup1, tup2, tup3))
