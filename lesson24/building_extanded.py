from building import Building


class BuildingExtanded(Building):
    def __init__(self, name, floors, height, area, city):
        # super.__init__(name,floors,height,area,city)

        class Apartments:
            def __init__(self, numbers: int, residents: int, area: int):
                self.numbers = numbers
                self.residents = residents
                self.area = area

            def __str__(self):
                return f"{self.numbers}\n{self.residents}\n{self.area}"

            def add_apartment(self, number, resident_amout, area):
                return Apartments(number, resident_amout, area)

            def counter(self, new_num, new_amount):
                pass


Building = BuildingExtanded("atlat1", 13, 45, 600, "kiev")
print(BuildingExtanded(Apartments.add_apartment(355, 1020, 40)))
print(Building)
