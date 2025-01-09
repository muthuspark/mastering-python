def singleton(cls):
    instances = {}
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance

@singleton
class MySingleton:
    pass

instance1 = MySingleton()
instance2 = MySingleton()
print(instance1 is instance2) # Output: True