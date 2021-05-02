class MyRange:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __next__(self):
        next_one = self.start
        current_stop = self.stop

        for i in range(self.start, current_stop):
            while next_one < current_stop:
                next_one += self.step
                print(next_one, end=" <-> ")
            break


if __name__ == "__main__":
    ran = MyRange(0, 20, 3)
    print(next(ran))
