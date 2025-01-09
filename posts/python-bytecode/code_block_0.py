import dis

def my_function(a, b):
  c = a + b
  return c

dis.dis(my_function)