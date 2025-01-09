def make_bold(func):
  def wrapper(*args, **kwargs):
    return f"<b>{func(*args, **kwargs)}</b>"
  return wrapper

@make_bold
def get_message():
  return "Hello, world!"

print(get_message()) # Output: <b>Hello, world!</b>