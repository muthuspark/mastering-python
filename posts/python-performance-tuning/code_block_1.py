def linear_search(data, target):
    for item in data:
        if item == target:
            return True
    return False