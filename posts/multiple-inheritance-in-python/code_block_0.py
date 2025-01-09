class Parent1:
    def method1(self):
        print("Parent1 method")

class Parent2:
    def method2(self):
        print("Parent2 method")

class Child(Parent1, Parent2):  # Inherits from both Parent1 and Parent2
    def method3(self):
        print("Child method")

child_instance = Child()
child_instance.method1()  # Output: Parent1 method
child_instance.method2()  # Output: Parent2 method
child_instance.method3()  # Output: Child method