for i in range(0, 180):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count = count + 1
        if count == 42:
            break
    if count == 2:
        print(i)
