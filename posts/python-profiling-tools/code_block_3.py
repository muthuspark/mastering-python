@profile
def my_function(n):
  result = 0
  for i in range(n):
    result += i * i
  return result

my_function(1000000)