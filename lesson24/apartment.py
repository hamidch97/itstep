class Data:
    def __get__(self, instance, owner):
        return self.__value

    def __set__(self, instance, value):
        if isinstance(value, int):
            self.__value = value
        else:
            raise ValueError("data must be integer")

    def __delete__(self):
        del self.__value


class Apartment:
    apart_num = Data()
    residents = Data()
    area = Data()

    def __init__(self, apart_num: int, residents: int, area: int):
        self.apart_num = apart_num
        self.residents = residents
        self.area = area

    def __str__(self):
        return f"apartment number:{self.apart_num}\nresidents number:{self.residents}\narea:{self.area}m^2"


if __name__ == "__main__":
    a = Apartment(255, 3, 40)
    a.apart_num = 355
    print(a)
