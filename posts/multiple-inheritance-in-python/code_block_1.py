print(Child.mro()) # Output: [<class '__main__.Child'>, <class '__main__.Parent1'>, <class '__main__.Parent2'>, <class 'object'>]
print(Child.__mro__) # Output: (<class '__main__.Child'>, <class '__main__.Parent1'>, <class '__main__.Parent2'>, <class 'object'>, <class 'type'>)
