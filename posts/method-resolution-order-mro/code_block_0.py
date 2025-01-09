class A:
    def method(self):
        print("A.method")

class B(A):
    def method(self):
        print("B.method")

b = B()
b.method()  # Output: B.method

print(B.__mro__) # Output: (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)