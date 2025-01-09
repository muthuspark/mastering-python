lines = ["line " + str(i) for i in range(100000)] #Many lines

with open('large_file.txt', 'w') as f:
    f.writelines(line + '\n' for line in lines) # Efficient for many lines
