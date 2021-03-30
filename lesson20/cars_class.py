class Car:
    model_name = None
    year = None
    engine = None
    color = None
    price = None
    made = None

    def __init__(self, model_name, year, color, engine, price, made):
        self.model_name = model_name
        self.year = year
        self.color = color
        self.engine = engine
        self.price = price
        self.made = made

    def __str__(self):
        return f"model car :{self.model_name}\nyear : {self.year}\nengine : {self.engine}\ncolor : {self.color}\nprice :" \
               f" {self.price}\nmade in : {self.made}"


Gelly = Car("gelly", "2012", "black", "1.6", "5500$", "china")
print(Gelly)
