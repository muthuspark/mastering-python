class ValidateMeta(type):
    def __new__(cls, name, bases, attrs):
        if 'required_attribute' not in attrs:
            raise AttributeError("Class must define 'required_attribute'")
        return super().__new__(cls, name, bases, attrs)


class ValidClass(metaclass=ValidateMeta):
    required_attribute = 42

class InvalidClass(metaclass=ValidateMeta):
    pass # This will raise an AttributeError
