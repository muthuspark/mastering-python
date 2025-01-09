class ParentSlotClass:
    __slots__ = ['name']
    def __init__(self, name):
        self.name = name


class ChildSlotClass(ParentSlotClass):
    __slots__ = ['name', 'age'] # Must include 'name' from parent
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
