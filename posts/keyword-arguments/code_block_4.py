def display_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_details(name="Frank", profession="Engineer", location="Silicon Valley")