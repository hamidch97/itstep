def beautiful_list_generator(lst: list, marker: str, file_name: str) -> bool:
    with open(file_name) as f:
        # res = ""
        for line in f:
            f[line] = marker + f.write([lst][line])

    return f


dc_heroes = [
    "batman",
    "superman",
    "flash"
]
beautiful_list_generator(dc_heroes, "\u2713", "heroes.txt")
