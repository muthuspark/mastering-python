class EvenNumbers:
    def __init__(self, max):
        self.max = max
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max:
            result = self.current
            self.current += 2
            return result
        else:
            raise StopIteration

for number in EvenNumbers(10):
    print(number) # Output: 0 2 4 6 8 10
