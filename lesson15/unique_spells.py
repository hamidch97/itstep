def unique_spells(ron_spells: set, harry_spells: set) -> set:
    return ron_spells.symmetric_difference(harry_spells)


Ron = {"Accio", "Wingardium Leviosa", "Alohomora"}
Harry = {"Accio", "Wingardium Leviosa", "Expelliarmus", "Expecto patronum"}
print(unique_spells(Ron, Harry))
