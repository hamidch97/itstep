pyramid_size = int(input("enter size"))
for i in range(1, pyramid_size + 1):
    print(" " * (pyramid_size + 1 - i) + "*" * i + "*" * (i - 1))
