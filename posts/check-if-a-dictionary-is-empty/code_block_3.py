nested_dict = {"a": {"b": 1}, "c": {}}

if not nested_dict["c"]:
    print("The inner dictionary 'c' is empty.")

if len(nested_dict["c"]) == 0:
    print("The inner dictionary 'c' is empty.")