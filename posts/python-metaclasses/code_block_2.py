import logging

logging.basicConfig(level=logging.INFO)

class LogMeta(type):
    def __new__(cls, name, bases, attrs):
        for name, method in attrs.items():
            if callable(method):
                def wrapper(*args, **kwargs):
                    logging.info(f"Calling method: {name}")
                    return method(*args, **kwargs)
                attrs[name] = wrapper
        return super().__new__(cls, name, bases, attrs)


class LoggedClass(metaclass=LogMeta):
    def my_method(self, x):
        return x * 2

instance = LoggedClass()
result = instance.my_method(5)
print(result) #Output: 10 (along with log messages)
