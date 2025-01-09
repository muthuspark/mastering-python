def outer():
    a = 10
    def inner():
        nonlocal a
        a = 20
    inner()
    print(a) # Output: 20

outer()