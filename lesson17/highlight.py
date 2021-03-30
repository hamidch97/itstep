def highlight(text: str, str_to_select: str,decoration: str) -> str:
    decoration = text.endswith(str_to_select,,len(text)+1)
    return decoration
quote = "guns.lot of guns"
print(highlight(quote,"guns" ,"**"))
