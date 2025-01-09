class InvalidInputError(Exception):
    pass

def process_input(data):
    if not data:
        raise InvalidInputError("Input cannot be empty")
    # ...rest of the processing...