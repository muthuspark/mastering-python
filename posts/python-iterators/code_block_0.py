class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

my_iterator = MyIterator([1, 2, 3, 4, 5])

for item in my_iterator:
    print(item)  # Output: 1 2 3 4 5

my_iterator = MyIterator([10, 20, 30])
print(next(my_iterator)) # Output: 10
print(next(my_iterator)) # Output: 20
print(next(my_iterator)) # Output: 30
#print(next(my_iterator)) # Raises StopIteration exception