import gc

a = []
b = []
a.append(b)
b.append(a)

del a
del b

gc.collect() # Garbage collection is needed to reclaim memory in this case.