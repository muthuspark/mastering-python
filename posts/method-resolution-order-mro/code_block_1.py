class A:
    def method(self):
        print("A.method")

class B:
    def method(self):
        print("B.method")

class C(A, B):
    pass

c = C()
c.method()  # Output: A.method

print(C.__mro__) # Output: (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)