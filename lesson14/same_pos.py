ind = []
result = {}


def same_pos(tuple1, tuple2, tuple3) -> dict:
    res = []
    global ind
    global result

    for i in tup1:
        for j in tup2:
            if j == i and j not in res:
                res.append(j)
            for k in tup3:
                if k == j and k not in res:
                    res.append(k)

                if i == j == k:
                    res = [i, j, k]
    for i in res:
        res.remove(i)
    ind = [3, 1]

    result = {res[i]: ind[i] for i in range(len(res))}
    return result


tup1 = (4, 2, 6, 7)
tup2 = (1, 2, 7, 2, 9)
tup3 = (2, 2, 2, 7, 1)

print(same_pos(tup1, tup2, tup3))
