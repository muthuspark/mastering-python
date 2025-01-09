class Grandparent:
    def method1(self):
        print("Grandparent method")

class Parent1(Grandparent):
    pass

class Parent2(Grandparent):
    pass

class Child(Parent1, Parent2):
    pass

child_instance = Child()
child_instance.method1() # Output: Grandparent method