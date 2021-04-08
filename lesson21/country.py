class Country:
    def __init__(self, name: str, capital: str, continent: str, population: int, cities_name: str):
        self.name = name
        self.capital = capital
        self.continent = continent
        self.population = population
        self.cities_name = cities_name

    def __str__(self):
        return f"country:{self.name}\ncapital:{self.capital}\ncontinent:{self.continent}\npopulation:{self.population}\n" \
               f"name of city:{self.cities_name}"

    def valid_data(self):
        if self.population < 0:
            raise ValueError("population country can not be negative")
        elif isinstance(self.name, int):
            raise ValueError("name must be string")
        elif isinstance(self.capital, int):
            raise ValueError("capital must be string")
        elif isinstance(self.continent, int):
            raise ValueError("continent must be string")
        elif isinstance(self.cities_name, int):
            raise ValueError("city names must be string")


if __name__ == "__main__":
    ukrain = Country("ukrain", "kiev", "europe", 6586786, "kiev")
    ukrain.valid_data()
    print(ukrain)
