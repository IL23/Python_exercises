class MyRange:

    def __init__(self, stop, start=0, step=1):
        self.start = start - step
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.step
        if (self.start < self.stop and self.step > 0) \
                or (self.start > self.stop and self.step < 0):
            return self.start
        else:
            raise StopIteration


for i in MyRange(11):
    print(i)

