with open("file_with-words.txt", "r") as f:
    res = f.read().split()
    print(len(res))
