def my_function(pos1, pos2, default_arg="default", *args, **kwargs):
  print(f"Positional 1: {pos1}")
  print(f"Positional 2: {pos2}")
  print(f"Default: {default_arg}")
  print(f"Arbitrary Positional: {args}")
  print(f"Arbitrary Keyword: {kwargs}")

my_function(1,2,third="3", fourth=4, fifth=5, sixth=6)