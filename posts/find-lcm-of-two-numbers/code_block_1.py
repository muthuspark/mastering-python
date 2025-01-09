def lcm_iterative(a, b):
  """
  Calculates the LCM of two numbers using an iterative approach.
  """
  if a > b:
    greater = a
  else:
    greater = b

  while(True):
    if((greater % a == 0) and (greater % b == 0)):
      lcm = greater
      break
    greater += 1
  return lcm

#Example Usage
num1 = 15
num2 = 20
print(f"The LCM of {num1} and {num2} using iterative method is: {lcm_iterative(num1, num2)}")
