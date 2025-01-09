print(records['name'])  # Accesses the 'name' field
print(records['age'])   # Accesses the 'age' field

print(records[0])       # Accesses the first record
print(records[0]['name']) # Accesses the 'name' field of the first record

tall_people = records[records['height'] > 1.75]
print(tall_people)