def func1(x):
    y = x * 2
    func2(y)

def func2(z):
    print(z)

func1(5)  # Output: 10