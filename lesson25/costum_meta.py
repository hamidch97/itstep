class CostumMeta(type):
    def __new__(self, name, bases, attributs):
        attribu = {}
        for key, value in attributs.items():
            if not key.startswith("__"):
                attribu["metod_" + key] = value
            else:
                attribu[key] = value
        return type(name, bases, attribu)

    def class_name(self):
        def __call__(self):
            new_name = self.name.lower
            return new_name

        return type(new_name,bases,attributs)


class Test(metaclass=CostumMeta):
    x = 10

    def get_x(self):
        return self.x


if __name__ == "__main__":
    a = Test()

    print(type(a))
