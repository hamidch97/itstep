try:
    # n is nember from 1 to 100
    n = int(input("enter nember from 1 to 100"))

    for i in range(1, n + 1):
        if n % 3 == 0:
            print("Fizz")
        if n % 5 == 0:
            print("Buzz")
        if n % 3 == 0 and n % 5 == 0:
            print("FuzzBuzz")
except Exception:
    print("Mistake ")
else:
    print("Mistake ")