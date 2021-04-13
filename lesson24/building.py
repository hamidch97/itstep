class Integer:
    def __get__(self, instance, owner):
        return self.__value

    def __set__(self, instance, value):
        if isinstance(value, (int)):
            self.__value = value
        else:
            raise ValueError("enter integer number please")

    def __delete__(self, obj):
        del self.__value


class StringCh:
    def __get__(self, instance, owner):
        return self.__value

    def __set__(self, instance, value):
        if isinstance(value, (str)):
            self.__value = value
        else:
            raise ValueError("enter string please")

    def __delete__(self, obj):
        del self.__value


class Building:
    name = StringCh()
    floors = Integer()
    height = Integer()
    area = Integer()
    city = StringCh()

    def __init__(self, name: str, floors: int, height: int, area: str, city: str):
        self.name = name
        self.floors = floors
        self.height = height
        self.area = area
        self.city = city

    def __str__(self):
        return f"name of building : {self.name}\nnumber of floors : {self.floors}\nheight : {self.height} m\narea : {self.area}m^2\ncity : {self.city}"


if __name__ == "__main__":
    b = Building("smarthous", 12, 69, 400, "kiev")
    b.name = "tizi"
    b.floors = 28
    print(b)
