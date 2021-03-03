def find_all_entry(text,symbol=True):
    res = []
    #symbol = ""
    for i in text:
        if i == symbol:
            return res.append(i)
    return res
text1 = "asufbiuysgb-89rg"
print(find_all_entry(text1,a))


