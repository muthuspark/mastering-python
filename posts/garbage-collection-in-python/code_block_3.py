import weakref

class MyClass:
    pass

obj = MyClass()
weak_ref = weakref.ref(obj)

print(weak_ref())  # Output: <__main__.MyClass object at ...>

del obj #Object deleted.

print(weak_ref()) # Output: None (object garbage collected)
