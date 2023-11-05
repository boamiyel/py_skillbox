class DoubleElement:
    def __init__(self, *lst):
        self.elements = iter(lst)

    def __next__(self):
        first = next(self.elements, None)
        second = next(self.elements, None)

        if first is not None and second is not None:
            return (first, second)
        else:
            raise StopIteration

    def __iter__(self):
        return self


dL = DoubleElement(1, 2, 3, 4)
for pair in dL:
    print(pair)

print()

dL = DoubleElement(1, 2, 3, 4, 5)
for pair in dL:
    print(pair)
