data = "name1:value1;name2:value2;name3:value3"
items = data.split(':', 2) #Splits only at the first two ':'
print(items) # Output: ['name1', 'value1', ';name2:value2;name3:value3']

items2 = data.split(':',1) #Splits only at the first ':'
print(items2) # Output: ['name1', 'value1;name2:value2;name3:value3']