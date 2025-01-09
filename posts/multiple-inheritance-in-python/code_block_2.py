class Parent1:
    def method1(self):
        print("Parent1 method")

class Parent2:
    def method1(self):
        print("Parent2 method")

class Child(Parent1, Parent2):
    pass

child_instance = Child()
child_instance.method1()  # Output: Parent1 method
