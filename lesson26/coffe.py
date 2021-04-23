from abc import abstractmethod


class Coffe:

    def __init__(self, name=None, milk=None):
        self.name = name
        self.milk = None

    @abstractmethod
    def get_cup_size(self):
        size = ["smal", "standart", "big"]
        print(f"choose size:\n1:{size[0]}\n2:{size[1]}\n3:{size[2]}")

    @abstractmethod
    def is_have_milk(self):

        if self.milk is not None:
            return True
        else:
            return False

    @abstractmethod
    def coffe_name(self):
        return f"name:{self.name}"


class Latte(Coffe):
    def __init__(self, name="latte", milk=not None):
        super().__init__(name, milk)
        self.name = "latte"
        self.milk = not None


class Cappuccino(Coffe):
    def __init__(self, name="cappuccino", milk=not None):
        super().__init__(name, milk)
        self.name = "cappuccino"
        self.milk = not None


class Black(Coffe):
    def __init__(self, name="black", milk=None):
        super().__init__(name, milk)
        self.name = "black"
        self.milk = None


class Espresso(Coffe):
    def __init__(self, name="espresso", milk=None):
        super().__init__(name, milk)
        self.name = "espresso"
        self.milk = None


class Mocha(Coffe):
    def __init__(self, name="mocha", milk=not None):
        super().__init__(name, milk)
        self.name = "mocha"
        self.milk = not None


if __name__ == "__main__":
    c = Coffe()
    c.get_cup_size()
    print(c.is_have_milk())
    print(c.coffe_name())
    print(c)

    l = Latte()
    print(l.get_cup_size())
    print(l.coffe_name())
    print(l.is_have_milk())
    print(l)

    capoccino =Cappuccino()
    print(capoccino.get_cup_size())
    print(capoccino.coffe_name())
    print(capoccino.is_have_milk())
    print(capoccino)
