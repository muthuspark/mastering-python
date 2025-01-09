import gc

a = []
b = []
a.append(b)
b.append(a)  # Cyclic reference

gc.collect() #Manually trigger garbage collection