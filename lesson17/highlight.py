def highlight(text: str, str_to_select: str, decoration: str) -> str:
    res = ""
    for i in text:
        if i == str_to_select:
            str_to_select.replace("**"+str_to_select+"**")
            print(text)



quote = "guns.lot of Guns"
print(highlight(quote, "guns", "**"))
