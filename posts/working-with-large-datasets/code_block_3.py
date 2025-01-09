def data_generator(filepath):
    with open(filepath, 'r') as f:
        next(f) # skip header if needed
        for line in f:
            # Process each line individually to extract relevant data
            yield process_line(line) #process_line is a helper function


for data_point in data_generator("large_dataset.csv"):
    #process data_point
    print(data_point)

