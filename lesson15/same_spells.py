def same_spells(ron_spells: set, harry_spells: set) -> set:
    return ron_spells.intersection(harry_spells)


Ron = {"Accio", "Wingardium Leviosa", "Alohomora"}
Harry = {"Accio", "Wingardium Leviosa", "Expelliarmus", "Expecto patronum"}
print(same_spells(Ron, Harry))
