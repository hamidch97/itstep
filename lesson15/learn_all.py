def learn_all(my_spells: set, teacher_spells: set) -> set:
    return my_spells | teacher_spells


Ron = {"Accio", "Wingardium Leviosa", "Alohomora"}
Harry = {"Accio", "Wingardium Leviosa", "Expelliarmus", "Expecto patronum"}

print(learn_all(Ron, Harry))
