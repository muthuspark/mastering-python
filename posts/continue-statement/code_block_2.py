for i in range(3):
    for j in range(3):
        if j == 1:
            continue #Skips j=1 in the inner loop
        print(f"i = {i}, j = {j}")