def add_new_spells(spells_list: set, *new_spell: set) -> bool:
    for i in spells_list:
        if new_spell in spells_list:
            spells_list.add(new_spell)

            return True
        else:
            return False

    return spells_list


Ron = {"Accio", "Wingardium Leviosa", "Alohomora"}

Harry = {"Accio", "Wingardium Leviosa", "Expelliarmus", "Expecto patronum"}

print(add_new_spells(Harry, "Expelliarmus", "Lumos", "Obliviate"))
print(Harry)
