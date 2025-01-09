class A:
    def method(self):
        print("A.method")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

d = D()
d.method()  # Output: A.method

print(D.__mro__) # Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
