class A:
    def method(self):
        print("A.method")

class B(A):
    pass

class C(A):
    def method(self):
        print("C.method")

class D(B, C):
    pass

d = D()
d.method()  # Output: C.method

print(D.__mro__) # Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)