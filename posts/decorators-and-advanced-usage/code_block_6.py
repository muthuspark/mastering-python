class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} to {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello_again():
    print("Hello again!")

say_hello_again()
say_hello_again()