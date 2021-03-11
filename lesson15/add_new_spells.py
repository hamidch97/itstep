def add_new_spell(spells_list: set, new_spell: str) -> bool:
    for i in spells_list:
        if new_spell not in spells_list:
            spells_list.add(new_spell)
            return True
        else:
            return False

    return spells_list


Ron = {"Accio", "Wingardium Leviosa", "Alohomora"}
Harry = {"Accio", "Wingardium Leviosa", "Expelliarmus", "Expecto patronum"}

print(add_new_spell(Ron, "Expelliarmus"))
print(Ron)
print(add_new_spell(Harry, "Expelliarmus"))
print(Harry)
